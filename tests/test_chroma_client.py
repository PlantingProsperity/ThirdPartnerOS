import pytest
import os
import shutil
import tempfile
from pathlib import Path
from src.brain.chroma_client import get_chroma_client, _reset_chroma_client

@pytest.fixture(scope="module")
def test_chroma_path():
    """Create a temporary directory for ChromaDB."""
    from config import ROOT_DIR
    tmp_dir = ROOT_DIR / "data" / "test_chroma_client"
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

def test_get_chroma_client():
    client = get_chroma_client()
    assert client is not None
    # Verify collections exist
    collections = client.list_collections()
    collection_names = [c.name for c in collections]
    assert "pinneo_brain" in collection_names
    assert "reference_library" in collection_names
