"""
Account Balance Manager

Part 1: Calculate final balances (only positive)
Part 2: Reject overdrafts, return balances + rejected list
Part 3: Platform covers shortfalls, return total coverage amount
"""

from collections import defaultdict
from typing import List, Dict, Tuple

# Change this import to test different parts
# from inputs1 import transactions, part

# from inputs2 import transactions, part

from inputs3 import transactions, part, platform_account_id


def get_account_balances(transactions: List[Dict]) -> Dict[str, int]:
    """
    Part 1: Calculate final balances for each account.
    Only return accounts with positive balance.
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    _act_bal = defaultdict(int)
    _act_user = defaultdict()
    for t in transactions:
        act_id = t["account_id"]
        amt = t["amount"]
        if _act_bal[act_id] + amt >= 0:
            _act_bal[act_id] += amt
        if _act_bal[act_id] == 0:
            del _act_bal[act_id]
    return _act_bal


def process_transactions(transactions: List[Dict]) -> Tuple[Dict[str, int], List[Dict]]:
    """
    Part 2: Process transactions, reject overdrafts.
    Returns: (balances dict, list of rejected transactions)
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    _act_bal = defaultdict(int)
    _act_user = defaultdict()
    _cancel_ts = []
    for t in transactions:
        act_id = t["account_id"]
        amt = t["amount"]
        if _act_bal[act_id] + amt >= 0:
            _act_bal[act_id] += amt
        else:
            # reject but add to _cancel_ts
            _cancel_ts.append(t)
    return _act_bal, _cancel_ts
    pass


def process_with_coverage(transactions: List[Dict], platform_account_id: str) -> int:
    """
    Part 3: Platform covers negative balances.
    Returns: total amount covered by platform
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    _act_bal = defaultdict(int)
    _act_user = defaultdict()
    _platform = defaultdict(int)
    _acc_pay = 0
    for t in transactions:
        act_id = t["account_id"]
        amt = t["amount"]
        if _act_bal[act_id] + amt >= 0:
            _act_bal[act_id] += amt
        else:
            # we will get the platform fee of the platform_account_id
            # reject but add to _cancel_ts
            if _act_bal[platform_account_id] + amt + _act_bal[act_id] >= 0:
                _act_bal[platform_account_id] += amt + _act_bal[act_id]
                _acc_pay += -(amt + _act_bal[act_id])
                _act_bal[act_id] = 0
    return _acc_pay


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
