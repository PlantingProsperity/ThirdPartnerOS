import pytest
import shutil
import os
from pathlib import Path
from dotenv import load_dotenv
from src.brain.embedder import PinneoEmbedder
from src.brain.chroma_client import _reset_chroma_client
from config import COLLECTION_PINNEO_BRAIN

# Load environment variables from .env
load_dotenv()

@pytest.fixture(scope="module")
def test_chroma_path():
    """Create a temporary directory for ChromaDB."""
    from config import ROOT_DIR
    tmp_dir = ROOT_DIR / "data" / "test_embedder"
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir(parents=True, exist_ok=True)
    yield tmp_dir
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)

@pytest.fixture(autouse=True)
def mock_chroma_path(test_chroma_path, monkeypatch):
    """Override CHROMA_DB_PATH and reset singleton."""
    monkeypatch.setattr("config.CHROMA_DB_PATH", test_chroma_path)
    _reset_chroma_client()

def test_embedder_hashing():
    embedder = PinneoEmbedder()
    # Create a temporary test file
    test_file = Path("test_hash.txt")
    test_file.write_text("test content")
    
    hash1 = embedder._get_file_hash(test_file)
    assert len(hash1) == 64 # SHA-256
    
    test_file.unlink()

def test_embedder_real_initialization():
    """Verify the embedder can initialize with real credentials."""
    embedder = PinneoEmbedder()
    assert embedder.genai_client is not None
