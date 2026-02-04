from typing import List, Dict, Tuple, Union


def find_fraudulent_merchants(
    non_fraud_codes: str,
    fraud_codes: str,
    mcc_thresholds: List[str],
    merchant_mcc_map: List[str],
    min_charges: str,
    charges: List[str],
) -> str:
    # --- Parse inputs ---
    non_fraud_set = set(filter(None, (c.strip() for c in non_fraud_codes.split(","))))
    fraud_set = set(filter(None, (c.strip() for c in fraud_codes.split(","))))

    # MCC -> threshold string/value
    mcc_to_threshold_str: Dict[str, str] = {}
    for row in mcc_thresholds:
        row = row.strip()
        if not row:
            continue
        mcc, thr = (x.strip() for x in row.split(",", 1))
        mcc_to_threshold_str[mcc] = thr

    acct_to_mcc: Dict[str, str] = {}
    for row in merchant_mcc_map:
        row = row.strip()
        if not row:
            continue
        acct, mcc = (x.strip() for x in row.split(",", 1))
        acct_to_mcc[acct] = mcc

    min_n = int(min_charges.strip())

    # Detect mode: ratio vs count (assumes input uses one style consistently)
    # If ANY threshold looks fractional (contains '.' or parses to <= 1), treat as ratio mode.
    ratio_mode = False
    for thr_s in mcc_to_threshold_str.values():
        s = thr_s.strip()
        if "." in s:
            ratio_mode = True
            break
        try:
            v = float(s)
            if v <= 1.0:
                ratio_mode = True
                break
        except ValueError:
            pass

    # Convert thresholds
    if ratio_mode:
        mcc_thr: Dict[str, float] = {
            mcc: float(s) for mcc, s in mcc_to_threshold_str.items()
        }
    else:
        mcc_thr_int: Dict[str, int] = {
            mcc: int(s) for mcc, s in mcc_to_threshold_str.items()
        }

    # --- State ---
    total_seen: Dict[str, int] = {}
    fraud_count: Dict[str, int] = {}
    is_fraudulent: Dict[str, bool] = {}

    # charge_id -> (account_id, was_fraudulent_at_time_of_charge)
    charge_index: Dict[str, Tuple[str, bool]] = {}

    def merchant_meets_rule(acct: str) -> bool:
        t = total_seen.get(acct, 0)
        if t < min_n:
            return False
        f = fraud_count.get(acct, 0)
        mcc = acct_to_mcc.get(acct)
        if mcc is None:
            return False  # if missing mapping, cannot evaluate

        if ratio_mode:
            thr = mcc_thr.get(mcc, 1.0)  # default "hard": only fraud if ratio >= 1
            return (f / t) >= thr if t > 0 else False
        else:
            thr = mcc_thr_int.get(mcc, 10**18)  # default "hard": effectively never
            return f >= thr

    # --- Process events in order ---
    for line in charges:
        line = line.strip()
        if not line:
            continue

        parts = [p.strip() for p in line.split(",")]
        event = parts[0]

        if event == "CHARGE":
            # CHARGE,charge_id,account_id,amount,code
            if len(parts) != 5:
                continue
            _, charge_id, acct, _amount, code = parts

            total_seen[acct] = total_seen.get(acct, 0) + 1

            is_fraud = code in fraud_set
            # (codes in non_fraud_set are just "not fraud"; unknown codes -> not fraud)
            if is_fraud:
                fraud_count[acct] = fraud_count.get(acct, 0) + 1

            charge_index[charge_id] = (acct, is_fraud)

            # Update status (once fraud => stays fraud unless a DISPUTE changes counts)
            if merchant_meets_rule(acct):
                is_fraudulent[acct] = True
            else:
                # do not flip from True->False here (Part 1/2 rule), only DISPUTE can restore
                is_fraudulent.setdefault(acct, False)

        elif event == "DISPUTE":
            # DISPUTE,charge_id
            if len(parts) != 2:
                continue
            _, charge_id = parts

            if charge_id not in charge_index:
                continue  # per prompt, should not happen

            acct, was_fraud = charge_index[charge_id]
            if was_fraud:
                # disputed charge becomes non-fraudulent: decrement fraud count once
                fraud_count[acct] = max(0, fraud_count.get(acct, 0) - 1)
                charge_index[charge_id] = (acct, False)

            # Recompute status — DISPUTE is the only thing allowed to restore
            is_fraudulent[acct] = merchant_meets_rule(acct)

        else:
            # Unknown event type; ignore
            continue

    fraudulent_accts = sorted([acct for acct, flag in is_fraudulent.items() if flag])
    return ",".join(fraudulent_accts)
