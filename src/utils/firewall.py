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
