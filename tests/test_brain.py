import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from src.brain.retriever import get_context, RetrievalResult
from config import COLLECTION_PINNEO_BRAIN

@pytest.fixture
def mock_genai():
    with patch("google.auth.default", return_value=(MagicMock(), "project-id")):
        with patch("google.genai.Client") as mock_client:
            # Mock embedding response
            mock_emb = MagicMock()
            mock_emb.embeddings = [MagicMock(values=[0.1]*768)]
            mock_client.return_value.models.embed_content.return_value = mock_emb
            yield mock_client

@pytest.fixture
def mock_chroma():
    with patch("src.brain.retriever.get_chroma_client") as mock_get_client:
        mock_client = MagicMock()
        mock_coll = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.get_collection.return_value = mock_coll
        
        # Mock query response
        mock_coll.query.return_value = {
            "ids": [["id1"]],
            "documents": [["test doc content"]],
            "metadatas": [[{"source_file": "test.md", "heading_text": "H1"}]],
            "distances": [[0.5]]
        }
        yield mock_coll

def test_retrieval_interface(mock_genai, mock_chroma):
    results = get_context("test query")
    assert len(results) == 1
    assert isinstance(results[0], RetrievalResult)
    assert results[0].text == "test doc content"
    assert "test.md" in results[0].citation
    assert results[0].score > 0
    assert results[0].low_confidence is False
