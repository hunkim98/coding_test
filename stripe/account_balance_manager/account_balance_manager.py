"""
Account Balance Manager

Part 1: Calculate final balances (only positive)
Part 2: Reject overdrafts, return balances + rejected list
Part 3: Platform covers shortfalls, return total coverage amount
"""

from typing import List, Dict, Tuple

# Change this import to test different parts
from inputs1 import transactions, part
# from inputs2 import transactions, part
# from inputs3 import transactions, part, platform_account_id


def get_account_balances(transactions: List[Dict]) -> Dict[str, int]:
    """
    Part 1: Calculate final balances for each account.
    Only return accounts with positive balance.
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def process_transactions(transactions: List[Dict]) -> Tuple[Dict[str, int], List[Dict]]:
    """
    Part 2: Process transactions, reject overdrafts.
    Returns: (balances dict, list of rejected transactions)
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def process_with_coverage(transactions: List[Dict], platform_account_id: str) -> int:
    """
    Part 3: Platform covers negative balances.
    Returns: total amount covered by platform
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Test runner
if __name__ == "__main__":
    if part == 1:
        result = get_account_balances(transactions)
        print(f"Balances: {result}")
        # Expected: {"account_A": 70, "account_C": 200}

    elif part == 2:
        balances, rejected = process_transactions(transactions)
        print(f"Balances: {balances}")
        print(f"Rejected: {rejected}")
        # Expected balances: {"account_A": 20, "account_B": 50}
        # Expected rejected: [{"account_id": "account_A", "amount": -150}, {"account_id": "account_B", "amount": -100}]

    elif part == 3:
        from inputs3 import platform_account_id
        total_coverage = process_with_coverage(transactions, platform_account_id)
        print(f"Total coverage: {total_coverage}")
        # Expected: 130
