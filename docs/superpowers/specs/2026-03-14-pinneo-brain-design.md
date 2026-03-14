# Design Spec: Pinneo Brain (Sprint 1A)

**Status:** Approved
**Date:** 2026-03-14
**Author:** Partner OS Architect (Gemini CLI)

## 1. Objective
Build a hybrid search retrieval system (The Pinneo Brain) that anchors all agent recommendations in Greg Pinneo's wisdom and legal reference material.

## 2. Architecture Overview
The system utilizes a hybrid approach combining semantic (dense) search and keyword (sparse) search over a local ChromaDB instance, orchestrated by the Memsearch library from Zilliz.

### Components
- **ChromaDB (v1.5.5):** Local persistent vector store.
- **Memsearch (v0.1.0):** Hybrid search interface (Dense + BM25 + Reranking).
- **Google Gemini text-embedding-004:** Vector generation via `google-genai` (OAuth).

## 3. Data Strategy
Knowledge is categorized into:
- **WISDOM:** Pinneo transcripts, CCIM modules. (Collection: `pinneo_brain`)
- **REFERENCE:** Zoning codes, municipal laws, PDFs. (Collection: `reference_library`)
- **LEARNED:** Summaries of closed deals (added via Learning Loop). (Collection: `pinneo_brain`)

### Ingestion Logic (`embedder.py`)
- **PDF Extraction:** Use `pdfplumber` to extract text from documents in `knowledge/reference/`.
- **Chunking Strategy:** 
    - **Markdown-Aware:** Splits at H1/H2 headers where possible.
    - **Constraints:** `CHUNK_SIZE: 800 characters`, `CHUNK_OVERLAP: 150 characters` (as defined in `config.py`).
- **Update Mode:** Incremental (SHA-256 hash-based). Only modified files are re-embedded.
- **Metadata Schema:**
    - `source_file` (str): Relative path to file.
    - `heading_text` (str): Text of the nearest parent header.
    - `heading_level` (int): Depth of the header.
    - `category` (str): WISDOM, REFERENCE, or LEARNED.
    - `hash` (str): SHA-256 hash of the source file.
    - `deal_id` (str, optional): For LEARNED outcomes.

## 4. Retrieval Logic (`retriever.py`)
- **Interface:** `get_context(query: str, collection: str = "pinneo_brain") -> List[Dict]`.
- **Hybrid Search:** Combines semantic neighborhood and keyword-specific terms via Memsearch.
- **Reranking Strategy:** 
    - Uses Memsearch's built-in `Reranker` (cross-encoder model).
    - Retrieves `RAG_TOP_K: 5` results (as defined in `config.py`).
- **Citation Contract:** Every result must include: `{source_file} | {heading_text}`.
- **Confidence Scoring:** Results with a relevance score below `LOW_CONFIDENCE_THRESHOLD: 0.40` must trigger a `LOW_CONFIDENCE: TRUE` flag in the agent output.

## 5. Storage (`chroma_client.py`)
- Initialized with `persist_directory` from `config.CHROMA_DB_PATH`.
- Manages collection existence and health checks.

## 6. Authentication & Client Initialization
All components must use the following pattern for Gemini API access:
```python
from google import genai
import google.auth
credentials, _ = google.auth.default()
client = genai.Client(credentials=credentials)
```
**No API keys are to be hardcoded or used.**

## 7. Error Handling & Resilience
- **API Failures (Gemini):** Implement exponential backoff for `text-embedding-004` calls. Fallback to `LOW_CONFIDENCE: TRUE` if unreachable after 3 retries.
- **Library Validation:** Verify `memsearch==0.1.0` (PyPI release March 2026) availability and initialization. If the library is unavailable or fails internal health checks, provide a temporary shim that uses raw ChromaDB `where` filters until a fix is applied.
- **PDF Corruption:** Gracefully skip unreadable PDFs and log errors to `src/utils/logger.py`.

## 8. Success Criteria
- `python -m pytest tests/test_brain.py` passes.
- A query for a known "Pinneo-ism" (e.g., "The Bird Letter") returns the correct source chunk in position 1.
- Reference material from a PDF is correctly retrieved with a file citation.
