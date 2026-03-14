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
