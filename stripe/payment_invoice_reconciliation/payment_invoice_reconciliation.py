"""
Payment Invoice Reconciliation

Step 1: Match by invoice ID in memo
Step 2: Match by exact amount (earliest date)
Step 3: Fuzzy match with forgiveness threshold

Priority: ID > Exact Amount > Fuzzy Amount
"""

from typing import List, Optional, Tuple

# Change this import to test different steps
from inputs1 import test_cases, step
# from inputs2 import test_cases, step
# from inputs3 import test_cases, step


def reconcile_payment(payment: str, invoices: List[str], forgiveness: int = 0) -> str:
    """
    Match a payment to an invoice.

    Args:
        payment: Payment string "id, amount, memo"
        invoices: List of invoice strings "id, date, amount"
        forgiveness: Tolerance for fuzzy matching (Step 3)

    Returns:
        Result string indicating match or no match
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def parse_payment(payment: str) -> Tuple[str, int, str]:
    """
    Parse payment string into components.

    Args:
        payment: "payment-id, amount, memo"

    Returns:
        Tuple of (payment_id, amount, memo)
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def parse_invoice(invoice: str) -> Tuple[str, str, int]:
    """
    Parse invoice string into components.

    Args:
        invoice: "invoice-id, date, amount"

    Returns:
        Tuple of (invoice_id, date, amount)
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def extract_invoice_id_from_memo(memo: str) -> Optional[str]:
    """
    Extract invoice ID from memo if present.
    Look for "paying for:" or "paying off:" (case-insensitive).

    Args:
        memo: Payment memo text

    Returns:
        Invoice ID if found, None otherwise
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def find_invoice_by_id(invoice_id: str, invoices: List[str]) -> Optional[Tuple[str, str, int]]:
    """
    Find invoice by ID.

    Args:
        invoice_id: ID to search for
        invoices: List of invoice strings

    Returns:
        Parsed invoice tuple if found, None otherwise
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def find_best_amount_match(
    invoices: List[str],
    amount: int,
    forgiveness: int = 0
) -> Optional[Tuple[str, str, int]]:
    """
    Find best matching invoice by amount.
    Exact matches have priority over fuzzy matches.
    Earliest date wins among same-priority matches.

    Args:
        invoices: List of invoice strings
        amount: Payment amount to match
        forgiveness: Tolerance for fuzzy matching

    Returns:
        Best matching invoice tuple, or None
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Test runner
def run_tests():
    print(f"Testing Step {step}")
    print("=" * 70)

    all_passed = True
    for i, tc in enumerate(test_cases):
        forgiveness = tc.get("forgiveness", 0)
        result = reconcile_payment(tc["payment"], tc["invoices"], forgiveness)
        expected = tc["expected"]
        passed = result == expected

        status = "✓" if passed else "✗"
        print(f"{status} Test {i + 1}")
        print(f"   Payment: {tc['payment']}")
        if forgiveness > 0:
            print(f"   Forgiveness: {forgiveness}")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
        print()

        if not passed:
            all_passed = False

    return all_passed


if __name__ == "__main__":
    run_tests()
