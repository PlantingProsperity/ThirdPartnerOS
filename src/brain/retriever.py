"""
Partner OS — Pinneo Brain Retriever
===================================

**Principal's Summary:**
The Retriever is the "Search Engine" for the Brain. When an agent (like the Manager) 
needs advice, it asks the Retriever. This tool looks through all the wisdom 
stored in the Brain, finds the most relevant advice, and presents it with 
clear citations so you can verify the source.

**Integration Note:**
Provides a hybrid-like retrieval interface over ChromaDB.
Combines semantic (dense) search with keyword-based scoring to 
ensure high-signal wisdom citations. Primary context source for all agent LLM calls.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from src.brain.chroma_client import get_chroma_client
from src.utils.logger import get_logger
from src.utils.genai_client import get_genai_client
from config import (
    COLLECTION_PINNEO_BRAIN, 
    RAG_TOP_K, 
    LOW_CONFIDENCE_THRESHOLD,
    GEMINI_EMBEDDING_MODEL
)

log = get_logger(__name__)

@dataclass
class RetrievalResult:
    """
    Structured container for a single retrieval result.
    """
    text: str
    citation: str
    score: float
    low_confidence: bool = False

def get_context(
    query: str, 
    collection_name: str = COLLECTION_PINNEO_BRAIN
) -> List[RetrievalResult]:
    """
    Retrieves relevant chunks from ChromaDB using semantic search
    and applies a keyword-relevance boost to simulate hybrid search.
    """
    log.info(f"Retrieving context for query: {query}")
    
    try:
        client = get_chroma_client()
        collection = client.get_collection(collection_name)
        
        # Initialize Gemini Client
        genai_client = get_genai_client()
        
        # 1. Generate Query Embedding
        response = genai_client.models.embed_content(
            model=GEMINI_EMBEDDING_MODEL,
            contents=query
        )
        query_embedding = response.embeddings[0].values
        
        # 2. Semantic Search (Dense)
        # We retrieve slightly more to allow for keyword-based reranking
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=RAG_TOP_K * 2,
            include=["documents", "metadatas", "distances"]
        )
        
        if not results["ids"] or not results["ids"][0]:
            return []

        # 3. Keyword-based Scoring (Simulated Hybrid/Reranking)
        # We look for exact keyword matches in the retrieved documents to boost relevance
        query_terms = set(query.lower().split())
        scored_results = []
        
        for i in range(len(results["ids"][0])):
            doc_text = results["documents"][0][i]
            metadata = results["metadatas"][0][i]
            # ChromaDB returns distances (lower is better). We convert to a similarity score (0-1).
            # Max distance is typically 2.0 for cosine similarity.
            distance = results["distances"][0][i]
            semantic_score = max(0, 1 - (distance / 2.0))
            
            # Keyword boost: count how many query terms appear in the document
            doc_terms = set(doc_text.lower().split())
            keyword_matches = len(query_terms.intersection(doc_terms))
            keyword_score = keyword_matches / len(query_terms) if query_terms else 0
            
            # Combined score (70% semantic, 30% keyword)
            final_score = (semantic_score * 0.7) + (keyword_score * 0.3)
            
            source = metadata.get("source_file", "Unknown")
            heading = metadata.get("heading_text", "Top Level")
            
            scored_results.append(RetrievalResult(
                text=doc_text,
                citation=f"{source} | {heading}",
                score=final_score,
                low_confidence=final_score < LOW_CONFIDENCE_THRESHOLD
            ))
            
        # 4. Sort and return top_k
        scored_results.sort(key=lambda x: x.score, reverse=True)
        return scored_results[:RAG_TOP_K]

    except Exception as e:
        log.error(f"Retrieval failure: {e}")
        return []
