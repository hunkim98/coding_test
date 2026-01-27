"""
Payment Reconciliation

Part 1: Parse payment JSON files
Part 2: Generate fixed-width clearing file
Part 3: Reconcile with bank transactions
Part 4: Handle disputes
"""

import json
from typing import List, Dict, Tuple

# Change this import to test different parts
from inputs1 import test_cases, part
# from inputs2 import test_cases, part
# from inputs3 import test_cases, part
# from inputs4 import test_cases, part


def parse_payments(json_str: str) -> Dict:
    """
    Part 1: Parse payment JSON and return summary statistics.

    Args:
        json_str: JSON string containing payment array

    Returns:
        Dict with count, total, by_merchant, by_currency
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def generate_clearing_file(payments: List[Dict], start_timestamp: int) -> str:
    """
    Part 2: Convert payments to fixed-width clearing file format.

    Format per line:
    - ARN: 22 digits (zero-padded, sequential from 1)
    - Timestamp: 20 digits (zero-padded, increment by 1)
    - Amount: 10 digits (zero-padded)
    - Currency: 3 lowercase letters

    Args:
        payments: List of payment dicts
        start_timestamp: Base timestamp in milliseconds

    Returns:
        Clearing file as newline-separated string
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def parse_clearing_entry(line: str) -> Tuple[str, int, int, str]:
    """
    Parse a clearing file line into components.

    Returns:
        Tuple of (arn, timestamp, amount, currency)
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def parse_bank_transaction(line: str) -> Tuple[str, int, int, str]:
    """
    Parse a bank transaction line into components.

    Returns:
        Tuple of (transaction_id, timestamp, amount, currency)
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def reconcile(clearing_entries: List[str], bank_transactions: List[str]) -> str:
    """
    Part 3: Match clearing entries with bank transactions.

    Args:
        clearing_entries: List of clearing file lines
        bank_transactions: List of bank transaction lines

    Returns:
        Reconciliation report as newline-separated string
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def reconcile_with_disputes(
    clearing_entries: List[str],
    bank_transactions: List[str],
    disputes: List[str]
) -> str:
    """
    Part 4: Reconcile with dispute handling.

    Args:
        clearing_entries: List of clearing file lines
        bank_transactions: List of bank transaction lines
        disputes: List of dispute lines

    Returns:
        Reconciliation report with DISPUTE status where applicable
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Test runner
def run_tests():
    print(f"Testing Part {part}")
    print("=" * 60)

    all_passed = True
    for i, tc in enumerate(test_cases):
        if part == 1:
            result = parse_payments(tc["json"])
            expected = tc["expected"]
            passed = result == expected
        elif part == 2:
            result = generate_clearing_file(tc["payments"], tc["start_ts"])
            expected = tc["expected"]
            passed = result == expected
        elif part == 3:
            result = reconcile(tc["clearing"], tc["bank"])
            expected = tc["expected"]
            passed = result == expected
        elif part == 4:
            result = reconcile_with_disputes(
                tc["clearing"], tc["bank"], tc["disputes"]
            )
            expected = tc["expected"]
            passed = result == expected
        else:
            continue

        status = "✓" if passed else "✗"
        print(f"{status} Test {i + 1}")
        print(f"   Expected:\n{expected}")
        print(f"   Got:\n{result}")
        print()

        if not passed:
            all_passed = False

    return all_passed


if __name__ == "__main__":
    run_tests()
