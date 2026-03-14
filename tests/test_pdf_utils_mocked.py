import sys
from unittest.mock import MagicMock
import pytest

# Mock pdfplumber before it can be imported by src.utils.pdf_utils
mock_pdfplumber = MagicMock()
sys.modules["pdfplumber"] = mock_pdfplumber

# Also need to mock src.utils.logger if it's not already handled,
# but it should be fine as it's part of the repo.

from src.utils.pdf_utils import extract_pdf_text

def test_extract_pdf_text_mocked():
    # Setup mock
    mock_pdf = MagicMock()
    mock_pdfplumber.open.return_value.__enter__.return_value = mock_pdf

    mock_page1 = MagicMock()
    mock_page1.extract_text.return_value = "Page 1 text"

    mock_page2 = MagicMock()
    mock_page2.extract_text.return_value = "Page 2 text"

    mock_page3 = MagicMock()
    mock_page3.extract_text.return_value = None # Should be ignored

    mock_pdf.pages = [mock_page1, mock_page2, mock_page3]

    # Execute
    result = extract_pdf_text("mock.pdf")

    # Verify
    assert result == "Page 1 text\nPage 2 text\n"
    mock_pdfplumber.open.assert_called_with("mock.pdf")

def test_extract_pdf_text_file_not_found():
    # Reset mock and set side effect
    mock_pdfplumber.open.side_effect = FileNotFoundError()

    with pytest.raises(FileNotFoundError):
        extract_pdf_text("missing.pdf")

    # Clean up for other tests
    mock_pdfplumber.open.side_effect = None
