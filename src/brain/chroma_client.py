"""
Partner OS — ChromaDB Client
============================
Initializes and manages the persistent ChromaDB vector store.
Provides direct access to WISDOM and REFERENCE collections.
"""

import chromadb
from pathlib import Path
from config import CHROMA_DB_PATH, COLLECTION_PINNEO_BRAIN, COLLECTION_REFERENCE_LIBRARY
from src.utils.logger import get_logger

log = get_logger(__name__)

def get_chroma_client() -> chromadb.PersistentClient:
    """
    Initializes and returns the persistent ChromaDB client.
    Ensures that the required collections exist before returning.
    """
    log.debug(f"Initializing ChromaDB client at {CHROMA_DB_PATH}")
    
    # Ensure parent directory exists
    CHROMA_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
    
    # Ensure default collections exist
    client.get_or_create_collection(name=COLLECTION_PINNEO_BRAIN)
    client.get_or_create_collection(name=COLLECTION_REFERENCE_LIBRARY)
    
    return client

def get_pinneo_collection() -> chromadb.Collection:
    """
    Convenience helper to retrieve the WISDOM (pinneo_brain) collection.
    """
    client = get_chroma_client()
    return client.get_collection(COLLECTION_PINNEO_BRAIN)

def get_reference_collection() -> chromadb.Collection:
    """
    Convenience helper to retrieve the REFERENCE (reference_library) collection.
    """
    client = get_chroma_client()
    return client.get_collection(COLLECTION_REFERENCE_LIBRARY)
