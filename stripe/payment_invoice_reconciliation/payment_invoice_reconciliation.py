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

from inputs2 import test_cases, step

from inputs3 import test_cases, step


def find_exact_match(
    pmt: str, amt: str, memo: str, pmt_to_inv: dict, pmt_amt: dict, inv_to_pmt: dict
):
    pfor_inv_id = None
    try:
        pfor_txt = "paying for: "
        pfor_loc = memo.lower().index(pfor_txt)
        inv_id_idx = memo.index("inv-")
        pfor_inv_id = memo[inv_id_idx:]
        pmt_amt[pmt] = int(amt)
        pmt_to_inv[pmt] = pfor_inv_id
        inv_to_pmt[pfor_inv_id] = pmt
    except:
        pass

    poff_inv_id = None
    try:
        poff_txt = "paying off: "
        poff_loc = memo.lower().index(poff_txt)
        inv_id_idx = memo.index("inv-")
        poff_inv_id = memo[inv_id_idx:]
        pmt_amt[pmt] = int(amt)
        pmt_to_inv[pmt] = poff_inv_id
        inv_to_pmt[poff_inv_id] = pmt
    except:
        pass
    return pfor_inv_id, poff_inv_id


def find_by_pmt(pmt: str, amt: str, pmt_to_inv: dict, inv_amt: dict, inv_due: dict):
    min_due = "9999-99-99"
    if pmt_to_inv.get(pmt) is not None:
        return
    for inv in inv_amt.keys():
        item = inv_amt[inv]
        if item == amt:
            if inv_due[inv] < min_due:
                pmt_to_inv[pmt] = inv
                min_due = inv_due[inv]


def find_forgive(
    pmt: str, amt: str, pmt_to_inv: dict, inv_amt: dict, inv_due: dict, forgiveness: int
):
    min_due = "9999-99-99"
    if forgiveness <= 0:
        return
    if pmt_to_inv.get(pmt) is not None:
        return
    for inv in inv_amt.keys():
        item = inv_amt[inv]
        if abs(item - amt) <= forgiveness:
            if inv_due[inv] < min_due:
                pmt_to_inv[pmt] = inv
                min_due = inv_due[inv]


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
    args = payment.split(",")
    pmt = args[0]
    amt = int(args[1].strip())
    memo = args[2]
    pfor_inv_id = None
    pmt_amt = {}
    pmt_to_inv = {}
    inv_to_pmt = {}
    inv_amt = {}
    inv_due = {}
    pmt_to_inv[pmt] = None

    for inv in invoices:
        args = inv.split(",")
        inv_id = args[0].strip()
        due = args[1].strip()
        inv_amt_item = int(args[2].strip())
        inv_amt[inv_id] = inv_amt_item
        inv_due[inv_id] = due

    pmt_amt[pmt] = amt
    pfor_inv_id, poff_inv_id = find_exact_match(
        pmt=pmt,
        amt=amt,
        memo=memo,
        pmt_to_inv=pmt_to_inv,
        pmt_amt=pmt_amt,
        inv_to_pmt=inv_to_pmt,
    )
    find_by_pmt(
        pmt=pmt, amt=amt, pmt_to_inv=pmt_to_inv, inv_amt=inv_amt, inv_due=inv_due
    )
    find_forgive(
        pmt=pmt,
        amt=amt,
        pmt_to_inv=pmt_to_inv,
        inv_amt=inv_amt,
        inv_due=inv_due,
        forgiveness=forgiveness,
    )

    # Get the first payment ID from the dictionary (Python 3 way)
    for val_pmt in pmt_to_inv.keys():
        val_amt = pmt_amt.get(val_pmt)
        val_inv = pmt_to_inv.get(val_pmt)
        val_due = inv_due.get(val_inv)
        if not val_due or not val_inv or not val_amt:
            return f"Payment {val_pmt} could not be matched to any invoice"
        return (
            f"Payment {val_pmt} paid {val_amt} for invoice {val_inv} due on {val_due}"
        )


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
