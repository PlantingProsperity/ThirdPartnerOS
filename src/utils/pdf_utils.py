"""
Partner OS — PDF Processing Utility
===================================
Handles text extraction from PDF documents using pdfplumber.
"""

import pdfplumber
from src.utils.logger import get_logger

log = get_logger(__name__)

def extract_pdf_text(pdf_path: str) -> str:
    """
    Extracts all text from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file.
        
    Returns:
        Extracted text as a single string.
        
    Raises:
        FileNotFoundError: If the PDF file is not found.
        Exception: For other extraction errors.
    """
    log.debug(f"Extracting text from PDF: {pdf_path}")
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except FileNotFoundError:
        log.error(f"PDF file not found: {pdf_path}")
        raise
    except Exception as e:
        log.error(f"Error extracting text from {pdf_path}: {e}")
        raise
        
    return text
