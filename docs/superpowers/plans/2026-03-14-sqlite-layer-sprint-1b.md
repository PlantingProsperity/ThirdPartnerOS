# SQLite Schema & Database Layer (Sprint 1B) Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish the relational core of Partner OS, providing a thread-safe Singleton connection and high-level Python helpers for all agent data operations.

**Architecture:** A Singleton database manager that enforces WAL mode and foreign keys, automatically bootstraps the schema from `schema.sql`, and provides a clean functional API for agents.

**Tech Stack:** `sqlite3` (Python Standard Library), `json`, `pathlib`.

---

### Chunk 1: Foundation & Initialization

#### Task 1: Initialize Singleton Connection & Schema Bootstrapping

**Files:**
- Create: `src/database/db.py`
- Test: `tests/test_db.py`

- [ ] **Step 1: Write the failing test**
```python
import pytest
import os
import shutil
from pathlib import Path
from src.database.db import get_db_connection, init_db
from config import DATABASE_PATH

@pytest.fixture(autouse=True)
def setup_teardown():
    if DATABASE_PATH.exists():
        os.remove(DATABASE_PATH)
    yield
    if DATABASE_PATH.exists():
        os.remove(DATABASE_PATH)

def test_init_db():
    init_db()
    assert DATABASE_PATH.exists()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    # Verify tables exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='deals'")
    assert cursor.fetchone() is not None
```

- [ ] **Step 2: Run test to verify it fails**
Run: `source .venv/bin/activate && pytest tests/test_db.py -v`
Expected: `ModuleNotFoundError` or `ImportError`

- [ ] **Step 3: Implement Singleton & Initialization in `src/database/db.py`**
```python
import sqlite3
import json
from pathlib import Path
from typing import Optional, List, Dict, Any, Union
from config import DATABASE_PATH, ROOT_DIR
from src.utils.logger import get_logger

log = get_logger(__name__)

_connection: Optional[sqlite3.Connection] = None

def get_db_connection() -> sqlite3.Connection:
    """Returns a singleton thread-safe SQLite connection with WAL enabled."""
    global _connection
    if _connection is None:
        DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
        # check_same_thread=False is safe because we use a singleton and SQLite handles locks
        _connection = sqlite3.connect(str(DATABASE_PATH), check_same_thread=False)
        _connection.row_factory = sqlite3.Row
        # Enable foreign keys and WAL mode for concurrent performance
        _connection.execute("PRAGMA foreign_keys = ON;")
        _connection.execute("PRAGMA journal_mode = WAL;")
    return _connection

def init_db():
    """Bootstraps the database schema from the root schema.sql file."""
    schema_path = ROOT_DIR / "schema.sql"
    if not schema_path.exists():
        log.error(f"Schema file not found at {schema_path}")
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    
    conn = get_db_connection()
    with open(schema_path, "r") as f:
        conn.executescript(f.read())
    conn.commit()
    log.info("Database initialized successfully.")
```

- [ ] **Step 4: Run test to verify it passes**
Run: `source .venv/bin/activate && pytest tests/test_db.py -v`
Expected: `PASS`

- [ ] **Step 5: Commit**
```bash
git add src/database/db.py tests/test_db.py
git commit -m "feat(database): implement singleton connection and schema bootstrapping"
```

---

### Chunk 2: Deal & File Management

#### Task 2: Implement Deal Management Helpers

**Files:**
- Modify: `src/database/db.py`
- Test: `tests/test_db.py`

- [ ] **Step 1: Write failing tests for Deal operations**
```python
def test_deal_lifecycle():
    from src.database.db import register_deal, update_deal_status, get_deal
    init_db()
    
    deal_id = register_deal("1234 Main St", "0001_1234_main_st", "/path/to/jacket")
    assert deal_id is not None
    
    deal = get_deal(deal_id)
    assert deal['address'] == "1234 Main St"
    assert deal['status'] == "INTAKE"
    
    update_deal_status(deal_id, "LIBRARIAN_PROCESSING")
    deal = get_deal(deal_id)
    assert deal['status'] == "LIBRARIAN_PROCESSING"
```

- [ ] **Step 2: Implement helpers in `src/database/db.py`**
```python
def register_deal(address: str, deal_code: str, jacket_path: str) -> int:
    """Registers a new deal in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO deals (address, deal_code, jacket_path) VALUES (?, ?, ?)",
        (address, deal_code, jacket_path)
    )
    conn.commit()
    return cursor.lastrowid

def update_deal_status(deal_id: int, status: str):
    """Updates the status of a deal."""
    conn = get_db_connection()
    conn.execute(
        "UPDATE deals SET status = ?, updated_at = datetime('now') WHERE id = ?",
        (status, deal_id)
    )
    conn.commit()

def get_deal(deal_id: int) -> Optional[sqlite3.Row]:
    """Retrieves a deal by ID."""
    conn = get_db_connection()
    return conn.execute("SELECT * FROM deals WHERE id = ?", (deal_id,)).fetchone()
```

- [ ] **Step 3: Run test to verify it passes**
Run: `source .venv/bin/activate && pytest tests/test_db.py -v`
Expected: `PASS`

- [ ] **Step 4: Commit**
```bash
git add src/database/db.py tests/test_db.py
git commit -m "feat(database): add deal management helpers"
```

#### Task 3: Implement File Indexing Helpers

**Files:**
- Modify: `src/database/db.py`
- Test: `tests/test_db.py`

- [ ] **Step 1: Write test for file indexing**
```python
def test_file_indexing():
    from src.database.db import register_deal, index_file, get_file_by_hash
    init_db()
    deal_id = register_deal("Test", "T001", "/tmp")
    
    file_id = index_file(deal_id, "/path/to/file.pdf", "file.pdf", "pdf", "hash123")
    assert file_id is not None
    
    file_record = get_file_by_hash("hash123")
    assert file_record['filename'] == "file.pdf"
```

- [ ] **Step 2: Implement helpers in `src/database/db.py`**
```python
def index_file(deal_id: Optional[int], file_path: str, filename: str, file_type: str, content_hash: str) -> int:
    """Records a new file in the index."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO files (deal_id, file_path, filename, file_type, content_hash) 
           VALUES (?, ?, ?, ?, ?)""",
        (deal_id, file_path, filename, file_type, content_hash)
    )
    conn.commit()
    return cursor.lastrowid

def get_file_by_hash(content_hash: str) -> Optional[sqlite3.Row]:
    """Retrieves a file record by its content hash."""
    conn = get_db_connection()
    return conn.execute("SELECT * FROM files WHERE content_hash = ?", (content_hash,)).fetchone()
```

- [ ] **Step 3: Run test to verify it passes**
Run: `source .venv/bin/activate && pytest tests/test_db.py -v`
Expected: `PASS`

- [ ] **Step 4: Commit**
```bash
git add src/database/db.py tests/test_db.py
git commit -m "feat(database): add file indexing helpers"
```

---

### Chunk 3: Agent Output & JSON Handling

#### Task 4: Implement Agent Output Helper with JSON support

**Files:**
- Modify: `src/database/db.py`
- Test: `tests/test_db.py`

- [ ] **Step 1: Write failing test for JSON serialization**
```python
def test_json_serialization():
    from src.database.db import register_deal, save_verdict, get_latest_verdict
    init_db()
    deal_id = register_deal("Verdict Test", "V001", "/tmp")
    
    citations = [{"source": "Pinneo 1", "page": 10}]
    save_verdict(deal_id, "APPROVE", 95, "Grounded reasoning.", citations)
    
    verdict = get_latest_verdict(deal_id)
    assert verdict['verdict'] == "APPROVE"
    assert isinstance(verdict['pinneo_citations'], list)
    assert verdict['pinneo_citations'][0]['source'] == "Pinneo 1"
```

- [ ] **Step 2: Implement JSON-aware helpers in `src/database/db.py`**
```python
def save_verdict(deal_id: int, verdict: str, confidence: int, reasoning: str, citations: List[Dict[str, Any]]):
    """Saves a Manager verdict with automatic JSON serialization of citations."""
    conn = get_db_connection()
    conn.execute(
        """INSERT INTO verdicts (deal_id, verdict, confidence_score, reasoning, pinneo_citations) 
           VALUES (?, ?, ?, ?, ?)""",
        (deal_id, verdict, confidence, reasoning, json.dumps(citations))
    )
    conn.commit()

def get_latest_verdict(deal_id: int) -> Optional[Dict[str, Any]]:
    """Retrieves the latest verdict for a deal with automatic JSON deserialization."""
    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM verdicts WHERE deal_id = ? ORDER BY issued_at DESC LIMIT 1", 
        (deal_id,)
    ).fetchone()
    
    if row:
        data = dict(row)
        if data.get('pinneo_citations'):
            data['pinneo_citations'] = json.loads(data['pinneo_citations'])
        return data
    return None
```

- [ ] **Step 3: Run test to verify it passes**
Run: `source .venv/bin/activate && pytest tests/test_db.py -v`
Expected: `PASS`

- [ ] **Step 4: Commit**
```bash
git add src/database/db.py tests/test_db.py
git commit -m "feat(database): add verdict helper with automatic JSON handling"
```
