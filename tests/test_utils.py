import pytest
from pathlib import Path
from src.utils.pdf_utils import extract_pdf_text
from src.utils.text_utils import chunk_markdown

def test_chunk_markdown_splitting():
    text = "# Header 1\nPara 1\n## Header 2\nPara 2"
    chunks = chunk_markdown(text, "test.md", "WISDOM", chunk_size=100, overlap=10)
    
    assert len(chunks) >= 2
    assert chunks[0]["metadata"]["heading_text"] == "Header 1"
    assert chunks[1]["metadata"]["heading_text"] == "Header 2"
    assert chunks[0]["metadata"]["category"] == "WISDOM"

def test_extract_pdf_text_exists():
    # Verify the function exists and doesn't crash on non-existent file (should handle gracefully)
    with pytest.raises(Exception):
        extract_pdf_text("non_existent.pdf")
