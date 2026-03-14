# Design Spec: SQLite Schema & Database Layer (Sprint 1B)

**Status:** Approved
**Date:** 2026-03-14
**Author:** Partner OS Architect (Gemini CLI)

## 1. Objective
Establish the relational core of Partner OS (the "State Bus"). This database serves as the shared notebook where all agents record deals, file indices, financial data, and agent outputs.

## 2. Architecture Overview
The database layer uses SQLite with a Singleton connection pattern to ensure efficient, thread-safe access for multiple agents.

### Components
- **SQLite (v3.x):** Local relational store.
- **WAL Mode:** Write-Ahead Logging enabled to support concurrent read/write operations.
- **Schema Bootstrapper:** Automatic execution of `schema.sql` on first initialization.

## 3. Data Integrity & Conventions
- **Foreign Keys:** Enforced via `PRAGMA foreign_keys = ON`.
- **JSON Handling:** Automatic serialization/deserialization for complex fields (citations, hierarchies, lists) using Python's `json` module within the helper layer.
- **Timestamping:** Consistent ISO 8601 format (YYYY-MM-DD HH:MM:SS) for all `created_at` and `updated_at` fields.

## 4. Database Helper (`src/database/db.py`)
Provides a clean, functional interface for agents to interact with the data without writing raw SQL.

### Core Functions
- `get_db_connection()`: Returns the singleton connection.
- `init_db()`: Bootstraps the schema from `schema.sql`.
- `register_deal(address, status)`: Creates a new deal and associated Deal Jacket metadata.
- `update_deal_status(deal_id, status)`: Moves a deal through the state machine.
- `index_file(deal_id, file_path, content_hash)`: Records a new file processed by the Librarian.
- `save_agent_output(table_name, data_dict)`: Generic helper for saving agent findings (CFO, Scout, Profiler, Manager).

## 5. Security & Validation
- **Parameterized Queries:** Mandatory for all writes to prevent SQL injection.
- **Path Validation:** All recorded file paths must be absolute and reside within authorized workspace directories.

## 6. Success Criteria
- `python -m pytest tests/test_db.py` passes.
- A full "Deal Lifecycle" test (Create Deal -> Index File -> Save Verdict) completes successfully.
- JSON fields are correctly retrieved as Python objects (lists/dicts).
