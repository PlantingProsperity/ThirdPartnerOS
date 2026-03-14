import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from src.brain.embedder import PinneoEmbedder
from config import COLLECTION_PINNEO_BRAIN

@pytest.fixture
def mock_genai():
    with patch("google.auth.default", return_value=(MagicMock(), "project-id")):
        with patch("google.genai.Client") as mock_client:
            yield mock_client

def test_embedder_hashing(mock_genai):
    embedder = PinneoEmbedder()
    # Create a temporary test file
    test_file = Path("test_hash.txt")
    test_file.write_text("test content")
    
    hash1 = embedder._get_file_hash(test_file)
    assert len(hash1) == 64 # SHA-256
    
    test_file.unlink()

def test_embedder_scaffold(mock_genai):
    embedder = PinneoEmbedder()
    assert embedder.client is not None
    assert embedder.genai_client is not None
