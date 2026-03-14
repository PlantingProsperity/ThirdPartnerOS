"""
Partner OS — SQLite Database Interface
=======================================
Manages the SQLite connection and provides typed helper functions for
all database operations used across the codebase.

Rules enforced here:
    - PRAGMA foreign_keys = ON is set on every connection.
    - PRAGMA journal_mode = WAL is set for concurrent read safety.
    - All writes use parameterized queries. String formatting is forbidden.
    - The schema is initialised from schema.sql on first run.

Usage:
    from src.database.db import get_connection, initialise_database

    initialise_database()  # call once at startup
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM deals WHERE status = ?", ("INTAKE",)
        ).fetchall()
"""

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Generator

from config import DATABASE_PATH, ROOT_DIR
from src.utils.logger import get_logger

log = get_logger(__name__)

SCHEMA_PATH: Path = ROOT_DIR / "src" / "database" / "schema.sql"


def initialise_database() -> None:
    """
    Create all tables defined in schema.sql if they do not already exist.

    Safe to call on every startup — uses CREATE TABLE IF NOT EXISTS.
    Does not drop or alter existing tables.

    Args:
        None

    Returns:
        None

    Raises:
        FileNotFoundError: If schema.sql is not found at SCHEMA_PATH.
        sqlite3.Error: On any database error during initialisation.
    """
    raise NotImplementedError("initialise_database() is not yet implemented.")


@contextmanager
def get_connection() -> Generator[sqlite3.Connection, None, None]:
    """
    Context manager yielding a configured SQLite connection.

    Automatically commits on clean exit and rolls back on exception.
    Sets foreign_keys=ON and journal_mode=WAL on every connection.

    Args:
        None

    Yields:
        sqlite3.Connection: A configured database connection.

    Raises:
        sqlite3.Error: On connection failure.

    Example:
        with get_connection() as conn:
            rows = conn.execute("SELECT id FROM deals").fetchall()
    """
    raise NotImplementedError("get_connection() is not yet implemented.")
