import pytest
from pathlib import Path
from src.brain.embedder import PinneoEmbedder
from config import COLLECTION_PINNEO_BRAIN

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
    # We don't perform a real embed call here to save tokens in simple init test
    # but we verify the client object is created.
