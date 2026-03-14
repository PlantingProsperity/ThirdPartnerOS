"""
Partner OS — Pinneo Brain Embedder
==================================

**Principal's Summary:**
The Embedder is the system's "Reading Engine." It takes the documents you upload 
(transcripts, PDFs, etc.) and translates them into a language the AI can understand. 
It is "incremental," meaning it remembers which files it has already read and 
only processes new or changed documents, saving both time and API costs.

**Integration Note:**
Handles the incremental ingestion of knowledge material into ChromaDB.
Processes Markdown and PDF files, generates Gemini embeddings, and
manages SHA-256 hashes to prevent redundant processing.
"""

import hashlib
from pathlib import Path
from typing import List, Dict
from google import genai
import google.auth
from src.brain.chroma_client import get_chroma_client
from src.utils.pdf_utils import extract_pdf_text
from src.utils.text_utils import chunk_markdown
from src.utils.logger import get_logger
from src.utils.genai_client import get_genai_client
from config import (
    CHUNK_SIZE, 
    CHUNK_OVERLAP, 
    GEMINI_EMBEDDING_MODEL,
    ROOT_DIR
)

log = get_logger(__name__)

class PinneoEmbedder:
    """
    Orchestrates the conversion of files into vectorized chunks.
    """
    
    def __init__(self):
        self.client = get_chroma_client()
        self.genai_client = get_genai_client()
        log.info("PinneoEmbedder initialized with Gemini API")

    def _get_file_hash(self, file_path: Path) -> str:
        """Calculates the SHA-256 hash of a file's contents."""
        return hashlib.sha256(file_path.read_bytes()).hexdigest()

    def ingest_directory(self, directory: Path, collection_name: str, category: str):
        """
        Recursively scans a directory and ingests new or modified files.
        """
        log.info(f"Starting ingestion for directory: {directory} into {collection_name}")
        
        if not directory.exists():
            log.warning(f"Directory does not exist: {directory}")
            return

        collection = self.client.get_collection(collection_name)
        
        for file_path in directory.rglob("*"):
            if not file_path.is_file():
                continue
                
            if file_path.suffix.lower() not in [".md", ".pdf"]:
                continue

            file_hash = self._get_file_hash(file_path)
            
            # Check if file has already been processed with this exact hash
            # We check the 'hash' field in the collection's metadata
            existing = collection.get(where={"hash": file_hash})
            if existing and existing["ids"]:
                log.debug(f"Skipping unmodified file: {file_path.name}")
                continue

            log.info(f"Processing file: {file_path}")
            
            # Extract text based on file type
            try:
                if file_path.suffix.lower() == ".pdf":
                    text = extract_pdf_text(str(file_path))
                else:
                    text = file_path.read_text(encoding="utf-8")
            except Exception as e:
                log.error(f"Failed to extract text from {file_path}: {e}")
                continue

            # Convert relative path for metadata
            # Ensure we are using absolute paths for relative_to calculation
            abs_file_path = file_path.resolve()
            try:
                rel_path = str(abs_file_path.relative_to(ROOT_DIR.resolve()))
            except ValueError:
                # Fallback if file is outside ROOT_DIR (e.g. in /tmp during tests)
                rel_path = file_path.name
            
            # Chunk the text
            chunks = chunk_markdown(
                text, 
                rel_path, 
                category, 
                CHUNK_SIZE, 
                CHUNK_OVERLAP
            )
            
            log.debug(f"Generated {len(chunks)} chunks for {file_path.name}")

            # Embed and Upsert
            for i, chunk in enumerate(chunks):
                try:
                    # Generate embedding via text-embedding-004
                    response = self.genai_client.models.embed_content(
                        model=GEMINI_EMBEDDING_MODEL,
                        contents=chunk["text"]
                    )
                    embedding = response.embeddings[0].values
                    
                    # Add file hash to metadata for future incremental checks
                    chunk["metadata"]["hash"] = file_hash
                    
                    # Create a unique, collision-resistant ID
                    # Format: rel_path_chunkindex
                    chunk_id = f"{rel_path}_{i}"
                    
                    collection.upsert(
                        ids=[chunk_id],
                        embeddings=[embedding],
                        documents=[chunk["text"]],
                        metadatas=[chunk["metadata"]]
                    )
                except Exception as e:
                    log.error(f"Error embedding/upserting chunk {i} of {file_path.name}: {e}")
                    continue
                    
        log.info(f"Ingestion complete for {directory}")
