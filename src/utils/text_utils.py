"""
Partner OS — Text & Markdown Processing Utility
===============================================
Provides Markdown-aware chunking logic to preserve semantic hierarchy.
"""

import re
from typing import List, Dict
from src.utils.logger import get_logger

log = get_logger(__name__)

def chunk_markdown(
    text: str, 
    source_file: str, 
    category: str, 
    chunk_size: int = 800, 
    overlap: int = 150
) -> List[Dict]:
    """
    Splits Markdown text into semantically coherent chunks.
    Prioritizes splitting at H1/H2 headers.
    
    Args:
        text: The raw Markdown text to chunk.
        source_file: Relative path to the source file (for metadata).
        category: Knowledge category (WISDOM, REFERENCE, etc.).
        chunk_size: Target character length per chunk.
        overlap: Character overlap between adjacent chunks.
        
    Returns:
        A list of dictionaries, each containing 'text' and 'metadata'.
    """
    log.debug(f"Chunking Markdown file: {source_file}")
    
    # Pattern to match headers (H1 through H6)
    # We use re.MULTILINE to match at the beginning of lines
    header_pattern = r'(^#+\s+.*$)'
    
    # Split text while keeping the headers
    parts = re.split(header_pattern, text, flags=re.MULTILINE)
    
    chunks = []
    current_heading = "Top Level"
    current_level = 0
    
    for part in parts:
        if not part.strip():
            continue
            
        # Check if this part is a header
        if re.match(r'^#+\s+.*$', part):
            current_heading = part.strip("# ").strip()
            current_level = part.count("#")
            continue
            
        # This part is a content block. We further split it if it's too long.
        # We also prepend the current heading context to maintain semantic grounding.
        content = part.strip()
        
        if len(content) <= chunk_size:
            chunks.append({
                "text": content,
                "metadata": {
                    "source_file": source_file,
                    "heading_text": current_heading,
                    "heading_level": current_level,
                    "category": category
                }
            })
        else:
            # Recursive split long content by size with overlap
            start = 0
            while start < len(content):
                end = start + chunk_size
                chunk_text = content[start:end]
                
                chunks.append({
                    "text": chunk_text,
                    "metadata": {
                        "source_file": source_file,
                        "heading_text": current_heading,
                        "heading_level": current_level,
                        "category": category
                    }
                })
                
                start += chunk_size - overlap
                if start >= len(content):
                    break
                    
    return chunks
