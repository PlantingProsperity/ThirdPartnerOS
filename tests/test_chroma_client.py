import pytest
import os
import shutil
from pathlib import Path
from src.brain.chroma_client import get_chroma_client

@pytest.fixture(scope="module", autouse=True)
def cleanup_chroma():
    """Cleanup ChromaDB data before and after tests."""
    from config import CHROMA_DB_PATH
    if CHROMA_DB_PATH.exists():
        shutil.rmtree(CHROMA_DB_PATH)
    yield
    if CHROMA_DB_PATH.exists():
        shutil.rmtree(CHROMA_DB_PATH)

def test_get_chroma_client():
    client = get_chroma_client()
    assert client is not None
    # Verify collections exist
    collections = client.list_collections()
    collection_names = [c.name for c in collections]
    assert "pinneo_brain" in collection_names
    assert "reference_library" in collection_names
