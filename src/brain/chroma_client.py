"""
Partner OS — ChromaDB Client
============================

**Principal's Summary:**
This component manages the "Digital Memory" of the system. It creates and maintains 
the database files where all of Greg Pinneo's wisdom and local laws are stored as 
mathematical "fingerprints" (vectors). It ensures that the computer has a reliable 
place to store and find this information.

**Integration Note:**
Initializes and manages the persistent ChromaDB vector store.
Provides direct access to WISDOM and REFERENCE collections. Used by the 
Embedder (to write data) and the Retriever (to read data).
"""

import chromadb
from pathlib import Path
from typing import Optional
from config import CHROMA_DB_PATH, COLLECTION_PINNEO_BRAIN, COLLECTION_REFERENCE_LIBRARY
from src.utils.logger import get_logger

log = get_logger(__name__)

# Singleton client object
_client: Optional[chromadb.PersistentClient] = None

def get_chroma_client() -> chromadb.PersistentClient:
    """
    Initializes and returns the singleton persistent ChromaDB client.
    Ensures that the required collections exist before returning.
    """
    global _client
    if _client is None:
        log.debug(f"Initializing singleton ChromaDB client at {CHROMA_DB_PATH}")
        
        # Ensure parent directory exists
        CHROMA_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        
        _client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
        
        # Ensure default collections exist
        _client.get_or_create_collection(name=COLLECTION_PINNEO_BRAIN)
        _client.get_or_create_collection(name=COLLECTION_REFERENCE_LIBRARY)
    
    return _client

def _reset_chroma_client():
    """
    Resets the singleton client. Internal use only (primarily for testing).
    """
    global _client
    _client = None

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
