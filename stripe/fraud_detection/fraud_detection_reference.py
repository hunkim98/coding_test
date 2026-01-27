"""
Fraud Detection - Reference solution for 60-min timed test.

Strategy:
- Part 1 (~15 min): Basic count threshold
- Part 2 (~10 min): Change to ratio threshold
- Part 3 (~15 min): Add DISPUTE handling
- Buffer (~20 min): Debug, edge cases

Key insight: Don't create helper functions with 10 parameters.
Keep everything in one place where you can see it.
"""

from typing import List


def find_fraudulent_merchants(
    non_fraud_codes: str,
    fraud_codes: str,
    mcc_thresholds: List[str],
    merchant_mcc_map: List[str],
    min_charges: str,
    charges: List[str],
) -> str:
    # Parse inputs into sets/dicts
    fraud_set = set(fraud_codes.split(","))
    min_txns = int(min_charges)

    # MCC -> threshold (could be int or float)
    thresholds = {}
    use_ratio = False
    for row in mcc_thresholds:
        mcc, thresh = row.split(",")
        thresh_val = float(thresh)
        thresholds[mcc] = thresh_val
        if thresh_val < 1:
            use_ratio = True

    # Merchant -> MCC mapping
    merchant_mcc = {}
    for row in merchant_mcc_map:
        acct, mcc = row.split(",")
        merchant_mcc[acct] = mcc

    # Track state per merchant
    merchants = {}  # acct -> {"total": int, "fraud": int, "flagged": bool}

    # Track charges for DISPUTE lookups
    charge_info = {}  # charge_id -> {"acct": str, "was_fraud": bool}

    def check_fraud(acct):
        """Check if merchant should be flagged as fraudulent."""
        m = merchants[acct]
        if m["total"] < min_txns:
            return False
        thresh = thresholds[merchant_mcc[acct]]
        if use_ratio:
            ratio = m["fraud"] / m["total"] if m["total"] > 0 else 0
            return ratio >= thresh
        else:
            return m["fraud"] >= thresh

    # Process each event
    for event in charges:
        parts = event.split(",")
        event_type = parts[0]

        if event_type == "CHARGE":
            _, charge_id, acct, amount, code = parts
            is_fraud = code in fraud_set

            # Initialize merchant if first time seeing
            if acct not in merchants:
                merchants[acct] = {"total": 0, "fraud": 0, "flagged": False}

            # Update counts
            merchants[acct]["total"] += 1
            if is_fraud:
                merchants[acct]["fraud"] += 1

            # Track charge for potential DISPUTE
            charge_info[charge_id] = {"acct": acct, "was_fraud": is_fraud}

            # Check if now fraudulent
            if check_fraud(acct):
                merchants[acct]["flagged"] = True

        elif event_type == "DISPUTE":
            _, charge_id = parts
            info = charge_info[charge_id]
            acct = info["acct"]

            # Only matters if the original charge was fraudulent
            if info["was_fraud"]:
                # Move from fraud to non-fraud
                merchants[acct]["fraud"] -= 1
                info["was_fraud"] = False  # Can't dispute twice

                # Re-check fraud status (can be restored to non-fraud)
                merchants[acct]["flagged"] = check_fraud(acct)

    # Collect fraudulent merchants
    result = [acct for acct in merchants if merchants[acct]["flagged"]]
    return ",".join(sorted(result))


# Test runner
if __name__ == "__main__":
    from inputs1 import (
        non_fraud_codes as nf1, fraud_codes as f1,
        mcc_thresholds as t1, merchant_mcc_map as m1,
        min_charges as mc1, charges as c1
    )
    from inputs2 import (
        non_fraud_codes as nf2, fraud_codes as f2,
        mcc_thresholds as t2, merchant_mcc_map as m2,
        min_charges as mc2, charges as c2
    )
    from inputs3 import (
        non_fraud_codes as nf3, fraud_codes as f3,
        mcc_thresholds as t3, merchant_mcc_map as m3,
        min_charges as mc3, charges as c3
    )

    tests = [
        ("Part 1 (count)", nf1, f1, t1, m1, mc1, c1, "acct_1,acct_2"),
        ("Part 2 (ratio)", nf2, f2, t2, m2, mc2, c2, "acct_1,acct_3"),
        ("Part 3 (dispute)", nf3, f3, t3, m3, mc3, c3, "acct_2"),
    ]

    for name, nf, f, t, m, mc, c, expected in tests:
        result = find_fraudulent_merchants(nf, f, t, m, mc, c)
        status = "✓" if result == expected else "✗"
        print(f"{status} {name}: {result}")
        if result != expected:
            print(f"  Expected: {expected}")
