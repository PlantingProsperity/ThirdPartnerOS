# Pinneo Brain (Sprint 1A) Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a hybrid search retrieval system (The Pinneo Brain) using Memsearch and ChromaDB.

**Architecture:** A three-layer system consisting of a ChromaDB storage client, an incremental Markdown/PDF embedder, and a hybrid Memsearch retriever with reranking.

**Tech Stack:** `chromadb`, `memsearch`, `pdfplumber`, `google-genai`.

---

### Chunk 1: Project Setup & Foundation

#### Task 1: Initialize Project Scaffold & Dependencies

**Files:**
- Modify: `requirements.txt`
- Run: `python scaffold.py`

- [ ] **Step 1: Add `memsearch` to `requirements.txt`**
```bash
echo "memsearch==0.1.0" >> requirements.txt
```

- [ ] **Step 2: Initialize project directories and stub files**
Run: `python scaffold.py`
Expected: `src/`, `tests/`, `data/`, `logs/`, `staging/`, `deals/` directories created.

- [ ] **Step 3: Commit**
```bash
git add requirements.txt
git commit -m "chore: add memsearch dependency and initialize project scaffold"
```

#### Task 2: Initialize Persistent Storage (`chroma_client.py`)

**Files:**
- Create: `src/brain/chroma_client.py`
- Test: `tests/test_chroma_client.py`

- [ ] **Step 1: Write the failing test**
```python
import pytest
from src.brain.chroma_client import get_chroma_client

def test_get_chroma_client():
    client = get_chroma_client()
    assert client is not None
    collections = client.list_collections()
    collection_names = [c.name for c in collections]
    assert "pinneo_brain" in collection_names
    assert "reference_library" in collection_names
```

- [ ] **Step 2: Run test to verify it fails**
Run: `pytest tests/test_chroma_client.py`
Expected: `ModuleNotFoundError`

- [ ] **Step 3: Implement `src/brain/chroma_client.py`**
```python
import chromadb
from config import CHROMA_DB_PATH, COLLECTION_PINNEO_BRAIN, COLLECTION_REFERENCE_LIBRARY

def get_chroma_client():
    """Initializes and returns the persistent ChromaDB client."""
    client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
    client.get_or_create_collection(name=COLLECTION_PINNEO_BRAIN)
    client.get_or_create_collection(name=COLLECTION_REFERENCE_LIBRARY)
    return client

def get_pinneo_collection():
    return get_chroma_client().get_collection(COLLECTION_PINNEO_BRAIN)

def get_reference_collection():
    return get_chroma_client().get_collection(COLLECTION_REFERENCE_LIBRARY)
```

- [ ] **Step 4: Run test to verify it passes**
Run: `pytest tests/test_chroma_client.py`
Expected: `PASS`

- [ ] **Step 5: Commit**
```bash
git add src/brain/chroma_client.py tests/test_chroma_client.py
git commit -m "feat(brain): implement persistent chroma client with default collections"
```

---

### Chunk 2: Ingestion Layer

#### Task 3: Implement PDF & Markdown Utilities

**Files:**
- Create: `src/utils/pdf_utils.py`
- Create: `src/utils/text_utils.py`
- Test: `tests/test_utils.py`

- [ ] **Step 1: Implement PDF extraction and Markdown-aware chunking**
```python
# src/utils/pdf_utils.py
import pdfplumber

def extract_pdf_text(pdf_path: str) -> str:
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# src/utils/text_utils.py
import re
from typing import List, Dict

def chunk_markdown(text: str, source_file: str, category: str, chunk_size: int = 800, overlap: int = 150) -> List[Dict]:
    chunks = []
    sections = re.split(r'(^#+\s+.*$)', text, flags=re.MULTILINE)
    current_heading = "Top Level"
    current_level = 0
    
    for section in sections:
        if re.match(r'^#+\s+.*$', section):
            current_heading = section.strip("# ").strip()
            current_level = section.count("#")
            continue
        
        start = 0
        while start < len(section):
            end = start + chunk_size
            content = section[start:end]
            chunks.append({
                "text": content,
                "metadata": {
                    "source_file": source_file,
                    "heading_text": current_heading,
                    "heading_level": current_level,
                    "category": category
                }
            })
            start += chunk_size - overlap
            if start >= len(section): break
    return chunks
```

- [ ] **Step 2: Commit**
```bash
git add src/utils/pdf_utils.py src/utils/text_utils.py
git commit -m "feat(utils): add pdf and markdown processing utilities"
```

#### Task 4: Implement Full Incremental Embedder (`embedder.py`)

**Files:**
- Create: `src/brain/embedder.py`
- Test: `tests/test_embedder.py`

- [ ] **Step 1: Implement the `PinneoEmbedder` class with full logic**
```python
import hashlib
from pathlib import Path
from typing import List, Dict
from google import genai
import google.auth
from src.brain.chroma_client import get_chroma_client
from src.utils.pdf_utils import extract_pdf_text
from src.utils.text_utils import chunk_markdown
from config import CHUNK_SIZE, CHUNK_OVERLAP, GEMINI_EMBEDDING_MODEL

class PinneoEmbedder:
    def __init__(self):
        self.client = get_chroma_client()
        credentials, _ = google.auth.default()
        self.genai_client = genai.Client(credentials=credentials)

    def _get_file_hash(self, file_path: Path) -> str:
        return hashlib.sha256(file_path.read_bytes()).hexdigest()

    def ingest_directory(self, directory: Path, collection_name: str, category: str):
        collection = self.client.get_collection(collection_name)
        for file_path in directory.rglob("*"):
            if file_path.suffix.lower() in [".md", ".pdf"]:
                file_hash = self._get_file_hash(file_path)
                # Check if hash already exists to avoid redundant embeddings
                existing = collection.get(where={"hash": file_hash})
                if existing and existing["ids"]:
                    continue
                
                text = extract_pdf_text(str(file_path)) if file_path.suffix.lower() == ".pdf" else file_path.read_text()
                chunks = chunk_markdown(text, str(file_path.relative_to(directory.parent.parent)), category, CHUNK_SIZE, CHUNK_OVERLAP)
                
                for i, chunk in enumerate(chunks):
                    response = self.genai_client.models.embed_content(
                        model=GEMINI_EMBEDDING_MODEL,
                        content=chunk["text"]
                    )
                    embedding = response.embeddings[0].values
                    chunk["metadata"]["hash"] = file_hash
                    
                    collection.upsert(
                        ids=[f"{file_path.relative_to(directory.parent.parent)}_{i}"],
                        embeddings=[embedding],
                        documents=[chunk["text"]],
                        metadatas=[chunk["metadata"]]
                    )
```

- [ ] **Step 2: Commit**
```bash
git add src/brain/embedder.py
git commit -m "feat(brain): implement incremental embedder with full ingestion logic"
```

---

### Chunk 3: Retrieval Layer

#### Task 5: Implement Hybrid Search Retriever (`retriever.py`)

**Files:**
- Create: `src/brain/retriever.py`
- Test: `tests/test_brain.py`

- [ ] **Step 1: Implement `get_context` with Memsearch**
```python
from memsearch import HybridSearch, Reranker
from src.brain.chroma_client import get_chroma_client
from config import COLLECTION_PINNEO_BRAIN, RAG_TOP_K, LOW_CONFIDENCE_THRESHOLD, GEMINI_EMBEDDING_MODEL
from google import genai
import google.auth
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class RetrievalResult:
    text: str
    citation: str
    score: float
    low_confidence: bool = False

def get_context(query: str, collection_name: str = COLLECTION_PINNEO_BRAIN) -> List[RetrievalResult]:
    client = get_chroma_client()
    credentials, _ = google.auth.default()
    genai_client = genai.Client(credentials=credentials)
    
    response = genai_client.models.embed_content(model=GEMINI_EMBEDDING_MODEL, content=query)
    query_embedding = response.embeddings[0].values
    
    hybrid = HybridSearch(client.get_collection(collection_name))
    results = hybrid.search(
        query_text=query,
        query_embedding=query_embedding,
        top_k=RAG_TOP_K * 2
    )
    
    reranker = Reranker()
    ranked_results = reranker.rerank(query, results, top_k=RAG_TOP_K)
    
    formatted_results = []
    for res in ranked_results:
        formatted_results.append(RetrievalResult(
            text=res.document,
            citation=f"{res.metadata['source_file']} | {res.metadata['heading_text']}",
            score=res.score,
            low_confidence=res.score < LOW_CONFIDENCE_THRESHOLD
        ))
    return formatted_results
```

- [ ] **Step 2: Write end-to-end verification test**
```python
# tests/test_brain.py
import pytest
from src.brain.embedder import PinneoEmbedder
from src.brain.retriever import get_context
from pathlib import Path
from config import COLLECTION_PINNEO_BRAIN

def test_retrieval_accuracy():
    embedder = PinneoEmbedder()
    # Ingest foundations sample
    sample_file = Path("docs/knowledge/Pinneo/Masters Series/01_Foundations.md")
    embedder.ingest_directory(sample_file.parent, COLLECTION_PINNEO_BRAIN, "WISDOM")
    
    # Query for known term
    results = get_context("Foundation of Commercial Real Estate")
    assert len(results) > 0
    assert "01_Foundations.md" in results[0].citation
    assert results[0].score >= 0.40
```

- [ ] **Step 3: Commit**
```bash
git add src/brain/retriever.py tests/test_brain.py
git commit -m "feat(brain): implement hybrid search retriever and verify accuracy"
```
