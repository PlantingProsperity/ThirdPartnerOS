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
