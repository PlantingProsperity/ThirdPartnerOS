"""
Partner OS — The Librarian (Archivist Agent)
=============================================
The Librarian is the sole gatekeeper of all data entering Partner OS.
It is the only agent permitted to move, rename, or reorganise files
anywhere in the filesystem. No other agent performs file move operations.

The Librarian operates in two modes:

    Mode 1 — The Sweep:
        Reconciles staging/inbox/ and all deals/ directories against
        the SQLite file index. Processes all unindexed files: classifies
        content, routes to the correct Deal Jacket subdirectory, updates
        SQLite, and triggers downstream pipelines (Whisper for audio,
        PDF extractor for documents). Runs on startup and on demand.

    Mode 2 — UI Upload Handler:
        Receives a file already written to staging/inbox/ by the
        Streamlit UI and triggers an immediate targeted sweep.

The Librarian is the only component that creates Deal Jacket directories.

Usage:
    from src.agents.librarian import LibrarianAgent
    librarian = LibrarianAgent()
    librarian.run_sweep()
"""

from pathlib import Path

from config import (
    STAGING_INBOX_DIR,
    STAGING_UNRESOLVED_DIR,
    DEALS_DIR,
    DealStatus,
    FileStatus,
    ContentClass,
    DealSubdir,
)
from src.database.db import get_connection
from src.utils.logger import get_logger

log = get_logger(__name__)


class LibrarianAgent:
    """
    The Archivist. Sole filesystem authority for Partner OS.
    """

    def __init__(self) -> None:
        """Initialise the Librarian agent with verified directory paths."""
        raise NotImplementedError("LibrarianAgent.__init__() is not yet implemented.")

    def run_sweep(self) -> dict:
        """
        Execute a full reconciliation sweep of staging/ and deals/.

        Scans staging/inbox/ for unprocessed files. Classifies each file,
        determines deal association, and routes to the correct Deal Jacket.
        Then reconciles all deals/ subdirectories against the SQLite index.

        Args:
            None

        Returns:
            Summary dict: {processed: int, routed: int, unresolved: int, failed: int}
        """
        raise NotImplementedError("run_sweep() is not yet implemented.")

    def classify_file(self, file_path: Path) -> tuple[str, str]:
        """
        Determine the file_type and content_class of an ingested file.

        Args:
            file_path: Absolute path to the file to classify.

        Returns:
            A tuple of (file_type, content_class) using constants from config.py.
        """
        raise NotImplementedError("classify_file() is not yet implemented.")

    def determine_deal_association(
        self, file_path: Path, content_class: str
    ) -> int | None:
        """
        Attempt to identify which deal a file belongs to.

        Checks parent folder naming, filename patterns, and AI-assisted
        content classification as a last resort.

        Args:
            file_path: Absolute path to the file.
            content_class: The classified content type of the file.

        Returns:
            deal_id integer if association is determined, None if ambiguous.
        """
        raise NotImplementedError("determine_deal_association() is not yet implemented.")

    def route_file(
        self, file_path: Path, deal_id: int, content_class: str
    ) -> Path:
        """
        Move a file from staging/ to the correct Deal Jacket subdirectory.

        This is the only function in the system that moves files on disk.
        Validates that the destination path is inside the authorised deal
        directory before executing the move.

        Args:
            file_path: Current absolute path of the file (in staging/).
            deal_id: Database ID of the deal this file belongs to.
            content_class: Determines which subdirectory to route to.

        Returns:
            The new absolute path of the file after routing.

        Raises:
            ValueError: If the resolved destination path escapes the deal directory.
        """
        raise NotImplementedError("route_file() is not yet implemented.")

    def create_deal_jacket(self, address: str) -> tuple[int, Path]:
        """
        Create a new Deal Jacket directory and register the deal in SQLite.

        Creates the full subdirectory structure and an initial jacket.json.
        This is the only function that creates new Deal Jacket directories.

        Args:
            address: Property address, used to generate the deal_code slug.

        Returns:
            A tuple of (deal_id, jacket_path).
        """
        raise NotImplementedError("create_deal_jacket() is not yet implemented.")

    def update_jacket_json(self, deal_id: int) -> None:
        """
        Rewrite jacket.json for a deal to reflect current SQLite state.

        Called after any file routing or deal status change. jacket.json
        is the human-readable filesystem manifest for the deal.

        Args:
            deal_id: Database ID of the deal to update.

        Returns:
            None
        """
        raise NotImplementedError("update_jacket_json() is not yet implemented.")
