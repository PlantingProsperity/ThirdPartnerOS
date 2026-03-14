#!/usr/bin/env python3
"""
Partner OS — Project Scaffold
==============================
Run from the project root directory:
    python scaffold.py

Creates the complete Partner OS directory structure and all stub files
with proper docstrings. Does NOT overwrite files that already exist.
"""

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.resolve()
print(f"=== Partner OS Scaffold ===")
print(f"Project root: {PROJECT_ROOT}")
print()

created = []
skipped = []


def write_stub(relative_path: str, content: str) -> None:
    """Write a stub file if it does not already exist."""
    filepath = PROJECT_ROOT / relative_path
    if filepath.exists():
        skipped.append(relative_path)
        print(f"  skipped (exists): {relative_path}")
    else:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content, encoding="utf-8")
        created.append(relative_path)
        print(f"  created: {relative_path}")


# =============================================================================
# DIRECTORIES
# =============================================================================
print("Creating directories...")
dirs = [
    "docs",
    "knowledge/pinneo",
    "knowledge/ccim",
    "knowledge/reference",
    "knowledge/outcomes",
    "staging/inbox/unresolved",
    "deals",
    "data/chroma",
    "src/ui",
    "src/agents",
    "src/brain",
    "src/database",
    "src/integrations",
    "src/learning",
    "src/utils",
    "tests",
    "logs",
]
for d in dirs:
    (PROJECT_ROOT / d).mkdir(parents=True, exist_ok=True)
print("  ✓ Directories created\n")

# =============================================================================
# __init__.py FILES
# =============================================================================
print("Creating __init__.py files...")
packages = [
    "src", "src/ui", "src/agents", "src/brain",
    "src/database", "src/integrations", "src/learning",
    "src/utils", "tests",
]
for pkg in packages:
    write_stub(f"{pkg}/__init__.py", '"""Partner OS package."""\n')
print()

# =============================================================================
# src/utils/logger.py
# =============================================================================
print("Creating src/utils/ stubs...")
write_stub("src/utils/logger.py", '''\
"""
Partner OS — Centralised Logging
==================================
Configures and provides the application-wide logger used by all agents
and utilities. All modules import get_logger() from here.

Never use print() anywhere in the codebase. Use logging exclusively.

Usage:
    from src.utils.logger import get_logger
    log = get_logger(__name__)
    log.info("Librarian sweep started.")
"""

import logging
import sys
from pathlib import Path

from config import LOG_DIR, LOG_FORMAT, LOG_DATE_FORMAT, LOG_LEVEL


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger for the given module name.

    Args:
        name: The module name, typically passed as __name__.

    Returns:
        A logging.Logger instance writing to both console and a log file
        in the LOG_DIR directory.
    """
    raise NotImplementedError("get_logger() is not yet implemented.")
''')

# =============================================================================
# src/utils/firewall.py
# =============================================================================
write_stub("src/utils/firewall.py", '''\
"""
Partner OS — The Firewall (Law 1 Enforcement)
===============================================
Validates all agent-generated output before it is written to disk or
displayed in the UI. Enforces Law 1: Partner OS produces DRAFT-ONLY
outputs. No outbound action language is permitted in any system output.

Any string containing outbound action patterns (send, submit, sign,
execute, call, email, forward, transmit, etc.) is flagged and blocked.

Usage:
    from src.utils.firewall import validate_output, FirewallViolation

    try:
        clean_text = validate_output(agent_output)
    except FirewallViolation as e:
        log.error("Firewall blocked output: %s", e)
"""

from src.utils.logger import get_logger

log = get_logger(__name__)


class FirewallViolation(Exception):
    """Raised when agent output contains prohibited outbound action language."""
    pass


def validate_output(text: str, agent_name: str = "unknown") -> str:
    """
    Scan agent output for outbound action language and raise if found.

    Args:
        text: The raw text output from an agent to validate.
        agent_name: Name of the producing agent, used in error messages.

    Returns:
        The original text unchanged if validation passes.

    Raises:
        FirewallViolation: If any prohibited patterns are detected.
    """
    raise NotImplementedError("validate_output() is not yet implemented.")
''')
print()

# =============================================================================
# src/brain/
# =============================================================================
print("Creating src/brain/ stubs...")
write_stub("src/brain/chroma_client.py", '''\
"""
Partner OS — ChromaDB Connection Management
============================================
Manages the persistent ChromaDB client and provides access to the two
named collections used by Partner OS:

    - pinneo_brain:       WISDOM (Pinneo transcripts, CCIM, Outcomes)
    - reference_library:  REFERENCE (Zoning codes, laws, regulations)

All modules that need ChromaDB import from here. This ensures a single
connection is shared and collection names are never magic strings.

Usage:
    from src.brain.chroma_client import get_pinneo_collection
    collection = get_pinneo_collection()
"""

import chromadb
from chromadb.api.models.Collection import Collection

from config import (
    CHROMA_DB_PATH,
    COLLECTION_PINNEO_BRAIN,
    COLLECTION_REFERENCE_LIBRARY,
)
from src.utils.logger import get_logger

log = get_logger(__name__)


def get_chroma_client() -> chromadb.PersistentClient:
    """
    Return a persistent ChromaDB client backed by CHROMA_DB_PATH.

    Args:
        None

    Returns:
        A chromadb.PersistentClient instance. Creates the database
        directory if it does not exist.
    """
    raise NotImplementedError("get_chroma_client() is not yet implemented.")


def get_pinneo_collection() -> Collection:
    """
    Return the pinneo_brain ChromaDB collection, creating it if absent.

    Args:
        None

    Returns:
        The pinneo_brain Collection instance.
    """
    raise NotImplementedError("get_pinneo_collection() is not yet implemented.")


def get_reference_collection() -> Collection:
    """
    Return the reference_library ChromaDB collection, creating it if absent.

    Args:
        None

    Returns:
        The reference_library Collection instance.
    """
    raise NotImplementedError("get_reference_collection() is not yet implemented.")
''')

write_stub("src/brain/embedder.py", '''\
"""
Partner OS — Pinneo Brain Embedder (Sprint 1A)
===============================================
Reads all .md files from the knowledge/ directories, chunks them into
overlapping segments, generates vector embeddings via the Gemini API
(text-embedding-004 model), and stores them in the appropriate
ChromaDB collection.

This script builds the Pinneo Brain. Run it once after knowledge/
directories are populated, and again whenever new files are added.

Collections populated:
    - pinneo_brain:      knowledge/pinneo/, knowledge/ccim/, knowledge/outcomes/
    - reference_library: knowledge/reference/

Usage:
    python -m src.brain.embedder
    python -m src.brain.embedder --collection pinneo_brain
    python -m src.brain.embedder --dry-run
"""

import argparse
from pathlib import Path
from typing import Iterator

from config import (
    PINNEO_DIR,
    CCIM_DIR,
    REFERENCE_DIR,
    OUTCOMES_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    COLLECTION_PINNEO_BRAIN,
    COLLECTION_REFERENCE_LIBRARY,
    GEMINI_EMBEDDING_MODEL,
)
from src.brain.chroma_client import get_pinneo_collection, get_reference_collection
from src.utils.logger import get_logger

log = get_logger(__name__)


def chunk_text(text: str, chunk_size: int, overlap: int) -> Iterator[str]:
    """
    Split text into overlapping chunks of a maximum character length.

    Args:
        text: The full source text to chunk.
        chunk_size: Maximum number of characters per chunk.
        overlap: Number of characters to overlap between adjacent chunks.

    Yields:
        Individual text chunks as strings.
    """
    raise NotImplementedError("chunk_text() is not yet implemented.")


def embed_text(text: str) -> list[float]:
    """
    Generate a vector embedding for a text string using the Gemini API.

    Args:
        text: The text to embed. Should be a single chunk from chunk_text().

    Returns:
        A list of floats representing the embedding vector.

    Raises:
        google.api_core.exceptions.GoogleAPIError: On API failure.
    """
    raise NotImplementedError("embed_text() is not yet implemented.")


def embed_directory(
    directory: Path,
    collection_name: str,
    dry_run: bool = False,
) -> int:
    """
    Embed all .md files in a directory into a ChromaDB collection.

    Skips files whose content hash already exists in the collection.
    This makes the function safe to re-run after adding new files.

    Args:
        directory: Path to the directory containing .md files.
        collection_name: Name of the ChromaDB collection to write to.
        dry_run: If True, log what would be embedded without writing.

    Returns:
        Number of new chunks embedded.
    """
    raise NotImplementedError("embed_directory() is not yet implemented.")


def main() -> None:
    """
    CLI entry point. Parse arguments and run the embedding pipeline.
    """
    raise NotImplementedError("main() is not yet implemented.")


if __name__ == "__main__":
    main()
''')

write_stub("src/brain/retriever.py", '''\
"""
Partner OS — Pinneo Brain Retriever
=====================================
Provides the semantic query interface used by all agents to retrieve
relevant context from ChromaDB before generating any AI output.

Every agent must call retrieve_pinneo_context() or
retrieve_reference_context() before calling the Gemini API.
This grounds the agent reasoning in the Pinneo Brain rather than
in generic AI training data.

If retrieved chunks fall below LOW_CONFIDENCE_THRESHOLD, the result
is flagged and the calling agent must mark its output LOW_CONFIDENCE.

Usage:
    from src.brain.retriever import retrieve_pinneo_context

    result = retrieve_pinneo_context(
        query="motivated seller holding property 15 years, needs cash flow",
    )
    # result.chunks    -> list of relevant Pinneo text passages
    # result.citations -> list of source references
    # result.low_confidence -> bool
"""

from dataclasses import dataclass, field

from config import RAG_TOP_K, LOW_CONFIDENCE_THRESHOLD
from src.brain.chroma_client import get_pinneo_collection, get_reference_collection
from src.utils.logger import get_logger

log = get_logger(__name__)


@dataclass
class RetrievalResult:
    """
    Structured output from a ChromaDB semantic query.

    Attributes:
        query: The original query string.
        chunks: Retrieved text passages, ordered by relevance.
        citations: Source references matching each chunk.
        scores: Relevance scores for each chunk (0.0 to 1.0).
        low_confidence: True if best score is below LOW_CONFIDENCE_THRESHOLD.
    """
    query: str
    chunks: list[str] = field(default_factory=list)
    citations: list[str] = field(default_factory=list)
    scores: list[float] = field(default_factory=list)
    low_confidence: bool = False


def retrieve_pinneo_context(
    query: str,
    top_k: int = RAG_TOP_K,
) -> RetrievalResult:
    """
    Query the pinneo_brain collection for context relevant to a deal scenario.

    Args:
        query: Natural language description of the deal situation.
        top_k: Number of chunks to retrieve.

    Returns:
        A RetrievalResult containing chunks, citations, scores, and
        a low_confidence flag per Law 3.
    """
    raise NotImplementedError("retrieve_pinneo_context() is not yet implemented.")


def retrieve_reference_context(
    query: str,
    top_k: int = RAG_TOP_K,
) -> RetrievalResult:
    """
    Query the reference_library collection for regulatory context.

    Args:
        query: Natural language query about regulations or legal requirements.
        top_k: Number of chunks to retrieve.

    Returns:
        A RetrievalResult containing relevant regulatory passages.
    """
    raise NotImplementedError("retrieve_reference_context() is not yet implemented.")
''')
print()

# =============================================================================
# src/database/db.py
# =============================================================================
print("Creating src/database/ stubs...")
write_stub("src/database/db.py", '''\
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
''')
print()

# =============================================================================
# src/agents/
# =============================================================================
print("Creating src/agents/ stubs...")

write_stub("src/agents/librarian.py", '''\
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
''')

write_stub("src/agents/cfo.py", '''\
"""
Partner OS — The CFO (Underwriter Agent)
==========================================
The Underwriter executes the three-phase CFO Hallucination Firewall:

    Phase 1 — EXTRACT (AI):
        Reads financial documents (T12s, OMs, rent rolls) from the deal
        documents/ directory. Uses the Gemini API to extract financial
        variables into a draft_financials SQLite record (status UNVERIFIED).
        Records a source citation for every number extracted.
        Advances deal status to AWAITING_VERIFICATION.

    Phase 2 — VERIFY (Human gate, enforced by the UI):
        The Streamlit UI presents extracted numbers with source citations.
        The principal reviews, corrects, and approves. This creates a
        verified_financials record and advances status to CFO_CALCULATING.
        The CFO agent does not participate in Phase 2.

    Phase 3 — CALCULATE (Pure Python, no AI):
        Reads verified_financials. Executes deterministic arithmetic only.
        Calculates Cap Rate, DSCR, LTV, Cash-on-Cash, IRR. Sets red-line
        flags. Then queries Pinneo Brain and calls Gemini to interpret
        results and recommend creative structuring options.

        WILL NOT RUN without a verified_financials record with status
        VERIFIED. This check is enforced at the start of every calculation.

Usage:
    from src.agents.cfo import CFOAgent
    cfo = CFOAgent()
    cfo.run_phase_1(deal_id=42)
    cfo.run_phase_3(deal_id=42)   # Only after principal verifies in UI
"""

from config import DealStatus, VerificationStatus
from src.database.db import get_connection
from src.brain.retriever import retrieve_pinneo_context
from src.utils.logger import get_logger
from src.utils.firewall import validate_output

log = get_logger(__name__)


class CFOAgent:
    """
    The Underwriter. Financial extraction, verification gate, and calculation.
    """

    def run_phase_1(self, deal_id: int) -> int:
        """
        Phase 1: Extract financial variables from deal documents using AI.

        Reads FINANCIAL_DOCUMENT and OFFERING_MEMORANDUM files from the
        deal jacket. Calls Gemini API to extract key variables with source
        citations. Writes draft_financials record (status UNVERIFIED).
        Advances deal status to AWAITING_VERIFICATION.

        Args:
            deal_id: Database ID of the deal to process.

        Returns:
            draft_financials record ID.

        Raises:
            ValueError: If deal is not in an eligible status for Phase 1.
        """
        raise NotImplementedError("run_phase_1() is not yet implemented.")

    def run_phase_3(self, deal_id: int) -> int:
        """
        Phase 3: Execute deterministic financial calculations (pure Python).

        WILL NOT EXECUTE without a verified_financials record (status VERIFIED).
        This is a hard check, not a convention.

        Calculates: Cap Rate, DSCR, LTV, Cash-on-Cash Return, IRR.
        Sets red-line flags. Then queries Pinneo Brain and calls Gemini
        to interpret results and recommend structuring options.

        Args:
            deal_id: Database ID of the deal to calculate.

        Returns:
            financial_analyses record ID.

        Raises:
            ValueError: If no VERIFIED financials record exists.
            ValueError: If deal status is not CFO_CALCULATING.
        """
        raise NotImplementedError("run_phase_3() is not yet implemented.")

    def _calculate_cap_rate(self, noi: float, purchase_price: float) -> float:
        """
        Calculate the Capitalization Rate: NOI / Purchase Price.

        Args:
            noi: Net Operating Income (annual, dollars).
            purchase_price: Property purchase price (dollars).

        Returns:
            Cap rate as a decimal (e.g. 0.065 for 6.5%).

        Raises:
            ValueError: If purchase_price is zero.
        """
        raise NotImplementedError("_calculate_cap_rate() is not yet implemented.")

    def _calculate_dscr(self, noi: float, annual_debt_service: float) -> float:
        """
        Calculate the Debt Service Coverage Ratio: NOI / Annual Debt Service.

        Red line: DSCR < 1.2 triggers flag_dscr_below_minimum.

        Args:
            noi: Net Operating Income (annual, dollars).
            annual_debt_service: Total annual principal and interest payments.

        Returns:
            DSCR as a float (e.g. 1.35).

        Raises:
            ValueError: If annual_debt_service is zero.
        """
        raise NotImplementedError("_calculate_dscr() is not yet implemented.")

    def _calculate_ltv(self, loan_amount: float, purchase_price: float) -> float:
        """
        Calculate the Loan-to-Value ratio: Loan Amount / Purchase Price.

        Red line: LTV > 0.75 triggers flag_ltv_above_maximum.

        Args:
            loan_amount: Total loan amount (dollars).
            purchase_price: Property purchase price (dollars).

        Returns:
            LTV as a decimal (e.g. 0.70 for 70%).

        Raises:
            ValueError: If purchase_price is zero.
        """
        raise NotImplementedError("_calculate_ltv() is not yet implemented.")
''')

write_stub("src/agents/scout.py", '''\
"""
Partner OS — The Scout (Intelligence Officer Agent)
====================================================
Hunts public records and market data for subject properties in
Clark County, WA. Detects motivated seller signals. Flags data
quality issues. Writes a structured scout_reports record to SQLite.

Tooling:
    - playwright:      Headless Chromium for JavaScript-rendered county sites
    - beautifulsoup4:  HTML parsing of rendered pages
    - pandas:          CSV ingestion for manually exported county records

Primary data source: Clark County Assessor portal
    https://www.clark.wa.gov/assessor

Motivated seller signals detected (Pinneo doctrine):
    - Ownership tenure >= 10 years (Pinneo Equity Screen Rule)
    - Tax delinquency
    - Expired or withdrawn MLS listings
    - Probate or estate indicators in ownership records
    - Suspicious rent estimates (flagged for human review)

Usage:
    from src.agents.scout import ScoutAgent
    scout = ScoutAgent()
    scout.run(deal_id=42)
"""

from pathlib import Path

from config import CLARK_COUNTY_ASSESSOR_URL, DealStatus
from src.database.db import get_connection
from src.brain.retriever import retrieve_pinneo_context
from src.utils.logger import get_logger

log = get_logger(__name__)


class ScoutAgent:
    """
    The Intelligence Officer. Public records retrieval and signal detection.
    """

    def run(self, deal_id: int) -> int:
        """
        Execute a full Scout run for a deal.

        Fetches property records from Clark County Assessor, detects
        motivated seller signals, and writes a scout_reports record.
        Advances deal status to PROFILER_RUNNING on completion.

        Args:
            deal_id: Database ID of the deal to investigate.

        Returns:
            scout_reports record ID.

        Raises:
            ValueError: If deal status is not SCOUT_RUNNING.
        """
        raise NotImplementedError("run() is not yet implemented.")

    def fetch_assessor_data(self, parcel_number: str) -> dict:
        """
        Scrape Clark County Assessor portal for a property record.

        Uses Playwright to render the site, then BeautifulSoup to parse.

        Args:
            parcel_number: Clark County parcel number for the subject property.

        Returns:
            A dict of raw property data fields from the assessor portal.

        Raises:
            RuntimeError: If the page fails to load or parse.
        """
        raise NotImplementedError("fetch_assessor_data() is not yet implemented.")

    def ingest_csv(self, csv_path: Path) -> dict:
        """
        Parse a manually exported CSV file of county records.

        Args:
            csv_path: Absolute path to the .csv file to parse.

        Returns:
            A dict of property data fields extracted from the CSV.
        """
        raise NotImplementedError("ingest_csv() is not yet implemented.")

    def score_motivated_seller(self, property_data: dict) -> tuple[int, dict]:
        """
        Calculate a motivated seller signal score (0-100) and flag dict.

        Applies the Pinneo Equity Screen and other signal detection rules.
        A score >= 60 is considered a strong motivated seller signal.

        Args:
            property_data: Raw property data from assessor or CSV ingest.

        Returns:
            A tuple of (score: int, flags: dict) mapping each signal to bool.
        """
        raise NotImplementedError("score_motivated_seller() is not yet implemented.")
''')

write_stub("src/agents/profiler.py", '''\
"""
Partner OS — The Profiler (Psychologist Agent)
================================================
Generates seller psychological archetypes by analysing all available
data about the seller: ownership history, Scout report, field audio
transcriptions, and correspondence found in the deal jacket.

Grounds every profile in retrieved Pinneo Brain context, specifically
the negotiation psychology heuristics and the Script Vault sections
of the Pinneo transcripts.

Output includes:
    - Pinneo psychological archetype (e.g. OLD_SCHOOL, ESTATE_HEIR)
    - Ordered pain hierarchy (what hurts most to least)
    - Leverage triggers (what motivates this seller to act)
    - Recommended negotiation approach
    - Relevant Pinneo verbatim scripts from the Master Rulebook
    - Risk flags (adversarial posture, attorney involvement, etc.)

Also checks seller_history in SQLite for prior deal interactions.

Usage:
    from src.agents.profiler import ProfilerAgent
    profiler = ProfilerAgent()
    profiler.run(deal_id=42)
"""

from config import DealStatus
from src.database.db import get_connection
from src.brain.retriever import retrieve_pinneo_context
from src.utils.logger import get_logger
from src.utils.firewall import validate_output

log = get_logger(__name__)


class ProfilerAgent:
    """
    The Psychologist. Seller archetype generation and negotiation strategy.
    """

    def run(self, deal_id: int) -> int:
        """
        Execute a full Profiler run for a deal.

        Gathers all available seller intelligence, queries the Pinneo
        Brain for relevant psychology heuristics, generates a
        seller_profiles record in SQLite. Advances deal status to
        MANAGER_SYNTHESIZING on completion.

        Args:
            deal_id: Database ID of the deal to profile.

        Returns:
            seller_profiles record ID.

        Raises:
            ValueError: If deal status is not PROFILER_RUNNING.
        """
        raise NotImplementedError("run() is not yet implemented.")

    def gather_seller_intelligence(self, deal_id: int) -> dict:
        """
        Collect all available seller data from SQLite and the deal jacket.

        Sources: scout_reports, transcripts/ directory, documents/
        (correspondence class), seller_history longitudinal table.

        Args:
            deal_id: Database ID of the deal.

        Returns:
            A consolidated dict of all seller intelligence for the Gemini call.
        """
        raise NotImplementedError("gather_seller_intelligence() is not yet implemented.")

    def assign_archetype(self, seller_intel: dict, pinneo_context: str) -> str:
        """
        Assign a Pinneo psychological archetype to the seller.

        Args:
            seller_intel: Consolidated seller data dict.
            pinneo_context: Retrieved Pinneo Brain context for psychology queries.

        Returns:
            Archetype string (e.g. "OLD_SCHOOL", "ESTATE_HEIR", "ADVERSARIAL").
        """
        raise NotImplementedError("assign_archetype() is not yet implemented.")
''')

write_stub("src/agents/manager.py", '''\
"""
Partner OS — The Manager (Chief of Staff Agent)
=================================================
The orchestrator and final voice of Partner OS. Synthesises all agent
outputs from SQLite, queries the Pinneo Brain, and issues the final
APPROVE or KILL verdict with a confidence score and plain English
reasoning grounded in Pinneo citations.

On APPROVE: also generates a complete, custom Letter of Intent (LOI)
as a .docx file, saved to the deal jacket drafts/ directory.
All LOI content is validated through the Firewall before saving.

On KILL: reasoning must include a conditions_to_flip field — a precise
enumerated list of what would have to be true to flip to APPROVE.

Usage:
    from src.agents.manager import ManagerAgent
    manager = ManagerAgent()
    manager.synthesise(deal_id=42)
"""

from config import DealStatus, Verdict
from src.database.db import get_connection
from src.brain.retriever import retrieve_pinneo_context
from src.utils.logger import get_logger
from src.utils.firewall import validate_output

log = get_logger(__name__)


class ManagerAgent:
    """
    The Chief of Staff. Synthesis, verdict issuance, and LOI generation.
    """

    def synthesise(self, deal_id: int) -> int:
        """
        Synthesise all agent outputs and issue the final APPROVE or KILL verdict.

        Reads financial_analyses, scout_reports, and seller_profiles from
        SQLite. Retrieves Pinneo Brain context. Calls Gemini API to reason
        over all inputs. Validates output through the Firewall. Writes a
        verdicts record to SQLite. Advances deal status to VERDICT_ISSUED.

        If verdict is APPROVE, also calls generate_loi().

        Args:
            deal_id: Database ID of the deal to synthesise.

        Returns:
            verdicts record ID.

        Raises:
            ValueError: If deal status is not MANAGER_SYNTHESIZING.
        """
        raise NotImplementedError("synthesise() is not yet implemented.")

    def generate_loi(self, deal_id: int, verdict_id: int) -> str:
        """
        Generate a custom Letter of Intent as a .docx file.

        Uses deal context, verdict reasoning, and Pinneo structuring
        recommendations to produce a complete LOI draft. Validates
        through the Firewall. Saves to deals/{deal_code}/drafts/.
        Writes an loi_drafts record to SQLite.

        Args:
            deal_id: Database ID of the deal.
            verdict_id: ID of the APPROVE verdict authorising this LOI.

        Returns:
            Absolute path to the generated .docx file as a string.
        """
        raise NotImplementedError("generate_loi() is not yet implemented.")

    def run_pattern_analysis(self) -> str:
        """
        Analyse deal_outcomes and archetype_performance for learning insights.

        Queries SQLite longitudinal tables. Surfaces patterns: which archetypes
        close most in Clark County, which Pinneo heuristics correlate with
        successful closings. Produces a plain English report for principals.

        Args:
            None

        Returns:
            Plain English pattern analysis report as a string.
        """
        raise NotImplementedError("run_pattern_analysis() is not yet implemented.")
''')
print()

# =============================================================================
# src/integrations/
# =============================================================================
print("Creating src/integrations/ stubs...")

write_stub("src/integrations/drive_sync.py", '''\
"""
Partner OS — Google Drive Sync (rclone Wrapper)
================================================
Wraps rclone to synchronise the Google Drive "Business with Brother"
folder to the local staging/ directory. Called by the Librarian before
running a sweep to ensure local staging/ reflects current Drive state.

rclone must be configured on this machine with a remote matching the
RCLONE_REMOTE_NAME config constant (default: "gdrive").
Confirm your remote name: rclone listremotes

Usage:
    from src.integrations.drive_sync import sync_from_drive
    result = sync_from_drive()
    print(f"Synced {result.files_transferred} new files.")
"""

import subprocess
from dataclasses import dataclass

from config import RCLONE_REMOTE_NAME, RCLONE_DRIVE_PATH, STAGING_DIR
from src.utils.logger import get_logger

log = get_logger(__name__)


@dataclass
class SyncResult:
    """
    Result of a rclone sync operation.

    Attributes:
        success: True if rclone exited with code 0.
        files_transferred: Number of files copied to staging/.
        error_message: stderr output if success is False.
    """
    success: bool
    files_transferred: int
    error_message: str = ""


def sync_from_drive() -> SyncResult:
    """
    Run rclone copy from the configured Google Drive remote to staging/.

    Uses rclone copy (not sync) to avoid deleting local files that have
    already been processed and moved into Deal Jackets by the Librarian.

    Args:
        None

    Returns:
        SyncResult with success status and transfer count.
    """
    raise NotImplementedError("sync_from_drive() is not yet implemented.")
''')

write_stub("src/integrations/whisper_transcriber.py", '''\
"""
Partner OS — Audio Transcription (OpenAI Whisper, CPU mode)
=============================================================
Transcribes audio files (.m4a, .mp3, .mp4, .wav) using OpenAI Whisper
running entirely on CPU. The GTX 580 (Fermi, nouveau driver) cannot
run Whisper on GPU — CPU mode is the correct and only option here.

Transcription output is saved as a .md file in the deal jacket
transcripts/ directory alongside the original audio file.

Model selection: the "base" Whisper model is recommended for the
i7-950 hardware. "small" is the practical maximum. "medium" and
larger will be prohibitively slow on this CPU.

Usage:
    from src.integrations.whisper_transcriber import transcribe_audio
    from pathlib import Path
    transcript_path = transcribe_audio(
        audio_path=Path("/path/to/field_recording.m4a"),
        deal_id=42,
    )
"""

from pathlib import Path

from config import DealSubdir
from src.utils.logger import get_logger

log = get_logger(__name__)

WHISPER_MODEL: str = "base"
"""
Whisper model to use for transcription.
Options: tiny, base, small, medium, large.
"base" recommended for the i7-950. "small" is the maximum practical size.
"""


def transcribe_audio(audio_path: Path, deal_id: int) -> Path:
    """
    Transcribe an audio file to text using Whisper (CPU mode only).

    Saves output as {original_stem}.md in the deal jacket transcripts/
    directory. Returns the path to the generated transcript file.

    Args:
        audio_path: Absolute path to the audio file to transcribe.
        deal_id: Database ID of the deal this audio belongs to.

    Returns:
        Absolute path to the generated .md transcript file.

    Raises:
        FileNotFoundError: If audio_path does not exist.
        RuntimeError: If Whisper transcription fails.
    """
    raise NotImplementedError("transcribe_audio() is not yet implemented.")
''')
print()

# =============================================================================
# src/learning/loop.py
# =============================================================================
print("Creating src/learning/ stubs...")
write_stub("src/learning/loop.py", '''\
"""
Partner OS — Continuous Learning Loop
=======================================
Implements the three-track learning system that allows Partner OS to
improve over decades of deal experience.

Track A — Outcome Recording:
    Records the final outcome (CLOSED or DEAD) of every deal in SQLite
    with full context: verdict accuracy, archetype accuracy, Pinneo
    heuristics cited, terms achieved, or failure reason.

Track B — Knowledge Reinforcement:
    For successfully closed deals, generates a structured .md summary
    in knowledge/outcomes/. Principals review and approve it. On approval,
    triggers the Librarian to embed it into the pinneo_brain ChromaDB
    collection. Future deals benefit from this experience exactly as
    they benefit from Pinneo lectures.

Track C — Pattern Analysis:
    On principal request, analyses deal_outcomes and archetype_performance
    to surface patterns. Delegated to the Manager agent.

Usage:
    from src.learning.loop import LearningLoop
    loop = LearningLoop()
    loop.record_outcome(deal_id=42, final_status="CLOSED", recorded_by="PRINCIPAL_1")
    loop.generate_knowledge_doc(deal_id=42)
"""

from pathlib import Path

from config import OUTCOMES_DIR
from src.database.db import get_connection
from src.utils.logger import get_logger

log = get_logger(__name__)


class LearningLoop:
    """Manages the three-track continuous learning system."""

    def record_outcome(
        self,
        deal_id: int,
        final_status: str,
        recorded_by: str,
        **outcome_fields,
    ) -> int:
        """
        Record the final outcome of a deal in SQLite (Track A).

        Args:
            deal_id: Database ID of the resolved deal.
            final_status: "CLOSED" or "DEAD".
            recorded_by: Which principal recorded this ("PRINCIPAL_1" or "PRINCIPAL_2").
            **outcome_fields: Additional outcome data (terms_achieved, failure_reason, etc.)

        Returns:
            deal_outcomes record ID.
        """
        raise NotImplementedError("record_outcome() is not yet implemented.")

    def generate_knowledge_doc(self, deal_id: int) -> Path:
        """
        Generate a .md knowledge document for a successfully closed deal (Track B).

        Reads deal data from SQLite and calls Gemini to produce a structured
        summary for embedding into the Pinneo Brain. Saves to knowledge/outcomes/
        for principal review before embedding.

        Args:
            deal_id: Database ID of the closed deal.

        Returns:
            Absolute path to the generated .md file in knowledge/outcomes/.

        Raises:
            ValueError: If the deal is not in CLOSED status.
        """
        raise NotImplementedError("generate_knowledge_doc() is not yet implemented.")

    def approve_and_embed_knowledge_doc(self, deal_id: int) -> None:
        """
        Embed an approved knowledge document into ChromaDB (Track B completion).

        Called by the principal via the Streamlit UI after reviewing the
        generated .md file. Triggers the Librarian embedder. Updates the
        deal_outcomes record with knowledge_doc_approved = 1.

        Args:
            deal_id: Database ID of the deal whose knowledge doc is approved.

        Returns:
            None
        """
        raise NotImplementedError(
            "approve_and_embed_knowledge_doc() is not yet implemented."
        )
''')
print()

# =============================================================================
# src/ui/app.py
# =============================================================================
print("Creating src/ui/ stubs...")
write_stub("src/ui/app.py", '''\
"""
Partner OS — Streamlit UI (V0.1 Frontend)
==========================================
The entire V0.1 user interface lives in this single file.

Streamlit renders a local web application in your browser tab.

Run with:
    streamlit run src/ui/app.py

The UI provides:
    - Deal dashboard: pipeline view, status tracking per deal
    - New deal intake: address entry and initial notes
    - File upload: writes to staging/inbox/ (Librarian handles routing)
    - Sweep trigger: manually run Librarian reconciliation
    - CFO verification form: review and approve extracted financials
    - Verdict display: APPROVE/KILL with confidence score and reasoning
    - LOI draft download: link to the generated .docx file
    - Outcome recording: close or kill a deal with structured outcome data
    - Learning loop: approve knowledge docs for ChromaDB embedding

All file movement, agent execution, and data writes are performed by
the backend agent modules. The UI reads state from SQLite and triggers
agent runs. The UI never moves files directly.
"""

import streamlit as st

from config import STAGING_INBOX_DIR, DEALS_DIR
from src.database.db import get_connection, initialise_database
from src.utils.logger import get_logger

log = get_logger(__name__)


def render_dashboard() -> None:
    """
    Render the main deal pipeline dashboard.

    Displays all active deals grouped by status, with key metrics
    and action buttons appropriate to each deal current state.

    Args:
        None

    Returns:
        None
    """
    raise NotImplementedError("render_dashboard() is not yet implemented.")


def render_file_upload() -> None:
    """
    Render the file upload interface.

    Accepts files via st.file_uploader, writes to staging/inbox/,
    and offers to trigger an immediate Librarian sweep.

    Args:
        None

    Returns:
        None
    """
    raise NotImplementedError("render_file_upload() is not yet implemented.")


def render_cfo_verification(deal_id: int) -> None:
    """
    Render the CFO financial verification form (Phase 2 gate).

    Displays each AI-extracted financial variable alongside its source
    citation. Allows the principal to correct values. The "Approve Numbers"
    button creates a verified_financials record and advances deal status.

    Args:
        deal_id: Database ID of the deal awaiting financial verification.

    Returns:
        None
    """
    raise NotImplementedError("render_cfo_verification() is not yet implemented.")


def main() -> None:
    """
    Streamlit entry point. Configure the page and render the active view.
    """
    st.set_page_config(
        page_title="Partner OS — The Third Partner",
        page_icon="🏢",
        layout="wide",
    )
    initialise_database()
    raise NotImplementedError("main() UI routing is not yet implemented.")


if __name__ == "__main__":
    main()
''')
print()

# =============================================================================
# TESTS
# =============================================================================
print("Creating tests/ stubs...")

write_stub("tests/test_brain.py", '''\
"""
Partner OS — Tests: Pinneo Brain Retrieval Quality
===================================================
Validates that the ChromaDB retriever returns relevant, high-quality
results for known deal scenarios.

Run AFTER Sprint 1A (embedder must have populated ChromaDB):
    python -m pytest tests/test_brain.py -v
"""

import pytest
from src.brain.retriever import retrieve_pinneo_context, RetrievalResult


def test_retrieval_returns_results() -> None:
    """Retriever returns at least one chunk for a clear deal query."""
    raise NotImplementedError("test not yet written.")


def test_motivated_seller_query_surfaces_equity_screen() -> None:
    """
    A query about a long-hold motivated seller should surface the
    Pinneo Equity Screen Rule (10+ years triggers creative financing).
    """
    raise NotImplementedError("test not yet written.")


def test_substitution_of_security_retrieval() -> None:
    """
    A query mentioning seller financing should surface the
    Substitution of Security concept from the Pinneo transcripts.
    """
    raise NotImplementedError("test not yet written.")


def test_low_confidence_flag_on_ambiguous_query() -> None:
    """
    A vague or off-topic query should return low_confidence=True.
    """
    raise NotImplementedError("test not yet written.")
''')

write_stub("tests/test_cfo.py", '''\
"""
Partner OS — Tests: CFO Deterministic Calculations
====================================================
Validates that all CFO Phase 3 financial formulas produce correct,
reproducible results and that the verification gate is enforced.

Run with:
    python -m pytest tests/test_cfo.py -v
"""

import pytest
from src.agents.cfo import CFOAgent


def test_cap_rate_calculation() -> None:
    """Cap Rate = NOI / Purchase Price. Verify with known values."""
    raise NotImplementedError("test not yet written.")


def test_dscr_calculation() -> None:
    """DSCR = NOI / ADS. Verify the 1.2 red-line flag triggers correctly."""
    raise NotImplementedError("test not yet written.")


def test_ltv_calculation() -> None:
    """LTV = Loan / Price. Verify the 0.75 red-line flag triggers correctly."""
    raise NotImplementedError("test not yet written.")


def test_phase_3_blocked_without_verified_financials() -> None:
    """Phase 3 must raise ValueError when no VERIFIED financials record exists."""
    raise NotImplementedError("test not yet written.")


def test_phase_3_calculation_is_deterministic() -> None:
    """Running Phase 3 twice on the same inputs must produce identical results."""
    raise NotImplementedError("test not yet written.")
''')

write_stub("tests/test_firewall.py", '''\
"""
Partner OS — Tests: Firewall Output Validation
================================================
Validates that the Firewall correctly identifies and blocks outbound
action language while passing clean agent output through unchanged.

Run with:
    python -m pytest tests/test_firewall.py -v
"""

import pytest
from src.utils.firewall import validate_output, FirewallViolation


def test_clean_analysis_passes() -> None:
    """Clean deal analysis text passes through the Firewall unchanged."""
    raise NotImplementedError("test not yet written.")


def test_send_verb_blocked() -> None:
    """Output containing the word send is blocked by the Firewall."""
    raise NotImplementedError("test not yet written.")


def test_sign_verb_blocked() -> None:
    """Output instructing to sign a document is blocked."""
    raise NotImplementedError("test not yet written.")


def test_email_verb_blocked() -> None:
    """Output instructing to email content externally is blocked."""
    raise NotImplementedError("test not yet written.")


def test_draft_label_passes() -> None:
    """Output explicitly labelled DRAFT is not blocked by the Firewall."""
    raise NotImplementedError("test not yet written.")
''')
print()

# =============================================================================
# .gitignore
# =============================================================================
print("Creating .gitignore...")
write_stub(".gitignore", """\
# Partner OS — .gitignore

# Python
__pycache__/
*.py[cod]
*.egg-info/
.env
venv/
.venv/

# Data — never commit the database or vector store
data/
*.db
*.sqlite

# Logs
logs/

# Deal Jackets — contain sensitive client data, never commit
deals/

# Staging — transient inbound files
staging/

# Knowledge base — large files, managed separately
knowledge/

# Streamlit
.streamlit/

# OS
.DS_Store
Thumbs.db
""")
print()

# =============================================================================
# SUMMARY
# =============================================================================
print("=" * 67)
print(f"Partner OS scaffold complete.")
print(f"  Files created:  {len(created)}")
print(f"  Files skipped:  {len(skipped)}")
print()
if created:
    print("Created:")
    for f in sorted(created):
        print(f"  {f}")
print()
print("Next steps:")
print("  1. Copy config.py, requirements.txt, schema.sql here")
print("  2. Copy GEMINI.md here")
print("  3. Copy PartnerOS_Architecture_v1.0.docx into docs/")
print("  4. Install dependencies (read requirements.txt header first)")
print("  5. Run: python -m pytest tests/ --collect-only")
print("=" * 67)
