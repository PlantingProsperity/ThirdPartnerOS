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
