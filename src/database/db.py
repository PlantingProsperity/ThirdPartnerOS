"""
Partner OS — SQLite Database Layer
==================================

**Principal's Summary:**
This component is the system's "Shared Notebook." It's where all the agents 
record their findings so they can stay in sync without talking to each other 
directly. It handles the storage of deals, files, and agent decisions in a 
reliable, organized way.

**Integration Note:**
Singleton thread-safe database manager. Enforces WAL mode and foreign keys. 
Provides the foundational state bus for all Partner OS agents.
"""

import sqlite3
import json
from pathlib import Path
from typing import Optional, List, Dict, Any, Union
from config import DATABASE_PATH, ROOT_DIR
from src.utils.logger import get_logger

log = get_logger(__name__)

# Singleton connection object
_connection: Optional[sqlite3.Connection] = None

def get_db_connection() -> sqlite3.Connection:
    """
    Returns a singleton thread-safe SQLite connection.
    Enables WAL mode and foreign key enforcement on initialization.
    """
    global _connection
    if _connection is None:
        log.debug(f"Connecting to database at {DATABASE_PATH}")
        
        # Ensure parent directory exists
        DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
        
        # Connect with thread-safety enabled for shared singleton
        _connection = sqlite3.connect(str(DATABASE_PATH), check_same_thread=False)
        
        # Return rows as dictionaries for easier agent integration
        _connection.row_factory = sqlite3.Row
        
        # Configure SQLite for performance and integrity
        _connection.execute("PRAGMA foreign_keys = ON;")
        _connection.execute("PRAGMA journal_mode = WAL;")
        
    return _connection

def init_db():
    """
    Bootstraps the database schema from the master schema.sql file.
    Must be called at system startup before any agent data is recorded.
    """
    schema_path = ROOT_DIR / "schema.sql"
    
    if not schema_path.exists():
        log.error(f"Critical Error: Database schema file not found at {schema_path}")
        raise FileNotFoundError(f"Database schema file missing: {schema_path}")
        
    log.info("Bootstrapping database schema...")
    conn = get_db_connection()
    
    try:
        with open(schema_path, "r") as f:
            schema_sql = f.read()
            conn.executescript(schema_sql)
        conn.commit()
        log.info("Database schema applied successfully.")
    except sqlite3.Error as e:
        log.error(f"Failed to apply database schema: {e}")
        raise

def register_deal(address: str, deal_code: str, jacket_path: str) -> int:
    """
    Registers a new deal in the master deal registry.
    
    Args:
        address: Human-readable address.
        deal_code: Unique deal identifier (e.g., 0042_1234_main_st).
        jacket_path: Absolute path to the deal jacket on disk.
        
    Returns:
        The integer ID of the newly created deal.
    """
    log.info(f"Registering new deal: {deal_code}")
    conn = get_db_connection()
    
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO deals (address, deal_code, jacket_path) 
            VALUES (?, ?, ?)
            """,
            (address, deal_code, jacket_path)
        )
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        log.error(f"Failed to register deal {deal_code}: {e}")
        raise

def update_deal_status(deal_id: int, status: str):
    """
    Updates the status of a deal in the state machine.
    
    Args:
        deal_id: The ID of the deal to update.
        status: The new status string (from config.py).
    """
    log.debug(f"Updating deal {deal_id} status to {status}")
    conn = get_db_connection()
    
    try:
        conn.execute(
            """
            UPDATE deals 
            SET status = ?, updated_at = datetime('now') 
            WHERE id = ?
            """,
            (status, deal_id)
        )
        conn.commit()
    except sqlite3.Error as e:
        log.error(f"Failed to update status for deal {deal_id}: {e}")
        raise

def get_deal(deal_id: int) -> Optional[sqlite3.Row]:
    """
    Retrieves a deal record by its ID.
    
    Args:
        deal_id: The ID of the deal.
        
    Returns:
        A sqlite3.Row object containing the deal data, or None if not found.
    """
    conn = get_db_connection()
    return conn.execute("SELECT * FROM deals WHERE id = ?", (deal_id,)).fetchone()

def index_file(
    deal_id: Optional[int], 
    file_path: str, 
    filename: str, 
    file_type: str, 
    content_hash: str
) -> int:
    """
    Records a new file in the system file index.
    
    Args:
        deal_id: The ID of the deal this file belongs to (optional).
        file_path: Absolute path to the file.
        filename: Name of the file.
        file_type: Type of file (audio, pdf, etc.).
        content_hash: SHA-256 hash of the content.
        
    Returns:
        The integer ID of the newly indexed file.
    """
    log.info(f"Indexing file: {filename} (Hash: {content_hash[:8]}...)")
    conn = get_db_connection()
    
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO files (deal_id, file_path, filename, file_type, content_hash) 
            VALUES (?, ?, ?, ?, ?)
            """,
            (deal_id, file_path, filename, file_type, content_hash)
        )
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        log.error(f"Failed to index file {filename}: {e}")
        raise

def get_file_by_hash(content_hash: str) -> Optional[sqlite3.Row]:
    """
    Retrieves a file record by its content hash.
    Used for duplicate detection during Librarian sweeps.
    
    Args:
        content_hash: The SHA-256 hash to look for.
        
    Returns:
        A sqlite3.Row object, or None if not found.
    """
    conn = get_db_connection()
    return conn.execute(
        "SELECT * FROM files WHERE content_hash = ?", 
        (content_hash,)
    ).fetchone()

def save_verdict(
    deal_id: int, 
    verdict: str, 
    confidence_score: int, 
    reasoning: str, 
    citations: List[Dict[str, Any]]
):
    """
    Saves a Manager agent verdict to the database.
    Automatically serializes the citations list to JSON.
    
    Args:
        deal_id: The ID of the deal.
        verdict: 'APPROVE' or 'KILL'.
        confidence_score: 0-100 score.
        reasoning: Plain English reasoning text.
        citations: List of source citation dictionaries.
    """
    log.info(f"Saving verdict {verdict} for deal {deal_id}")
    conn = get_db_connection()
    
    try:
        conn.execute(
            """
            INSERT INTO verdicts (deal_id, verdict, confidence_score, reasoning, pinneo_citations) 
            VALUES (?, ?, ?, ?, ?)
            """,
            (deal_id, verdict, confidence_score, reasoning, json.dumps(citations))
        )
        conn.commit()
    except sqlite3.Error as e:
        log.error(f"Failed to save verdict for deal {deal_id}: {e}")
        raise

def get_latest_verdict(deal_id: int) -> Optional[Dict[str, Any]]:
    """
    Retrieves the most recent verdict for a given deal.
    Automatically deserializes JSON fields into Python objects.
    
    Args:
        deal_id: The ID of the deal.
        
    Returns:
        A dictionary containing the verdict data, or None if not found.
    """
    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM verdicts WHERE deal_id = ? ORDER BY issued_at DESC LIMIT 1", 
        (deal_id,)
    ).fetchone()
    
    if not row:
        return None
        
    # Convert Row to dict so we can modify fields
    data = dict(row)
    
    # Auto-deserialize JSON fields
    if data.get("pinneo_citations"):
        data["pinneo_citations"] = json.loads(data["pinneo_citations"])
    if data.get("conditions_to_flip"):
        data["conditions_to_flip"] = json.loads(data["conditions_to_flip"])
        
    return data
