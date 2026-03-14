import pytest
from pathlib import Path
import shutil
import tempfile
from src.brain.embedder import PinneoEmbedder
from src.brain.retriever import get_context, RetrievalResult
from src.brain.chroma_client import get_chroma_client
from config import COLLECTION_PINNEO_BRAIN

@pytest.fixture(scope="module")
def test_chroma_path():
    """Create a temporary directory for ChromaDB."""
    tmp_dir = Path(tempfile.mkdtemp())
    yield tmp_dir
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)

@pytest.fixture(autouse=True)
def mock_chroma_path(test_chroma_path, monkeypatch):
    """Override CHROMA_DB_PATH in config for all tests."""
    monkeypatch.setattr("config.CHROMA_DB_PATH", test_chroma_path)

def test_pinneo_brain_end_to_end():
    """
    REAL PRODUCT TEST:
    1. Ingest a real Pinneo file.
    2. Query the brain for content in that file.
    3. Verify real API results and citations.
    """
    embedder = PinneoEmbedder()
    
    # Path to a real Pinneo foundation file
    sample_dir = Path("docs/knowledge/Pinneo/Masters Series")
    sample_file = sample_dir / "01_Foundations.md"
    
    if not sample_file.exists():
        pytest.skip(f"Sample file {sample_file} not found. Knowledge base must be present.")

    # 1. Real Ingestion (Calls Gemini API)
    # We create a temporary directory with just ONE file to speed up the test
    with tempfile.TemporaryDirectory() as tmp_ingest_dir:
        tmp_ingest_path = Path(tmp_ingest_dir)
        test_file_copy = tmp_ingest_path / "01_Foundations.md"
        shutil.copy(sample_file, test_file_copy)
        
        embedder.ingest_directory(tmp_ingest_path, COLLECTION_PINNEO_BRAIN, "WISDOM")
    
    # 2. Real Retrieval (Calls Gemini API)
    query = "What is the core philosophy of Greg Pinneo regarding commercial real estate?"
    results = get_context(query, COLLECTION_PINNEO_BRAIN)
    
    # 3. Validation
    assert len(results) > 0
    assert isinstance(results[0], RetrievalResult)
    assert results[0].score >= 0.30 # Realistic threshold for semantic matches
    assert "01_Foundations.md" in results[0].citation
    
    print(f"\n[TOP RESULT] {results[0].citation}")
    print(f"[PREVIEW] {results[0].text[:200]}...")
