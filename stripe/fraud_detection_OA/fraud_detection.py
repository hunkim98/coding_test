from collections import defaultdict
from inputs3 import (
    non_fraud_codes,
    fraud_codes,
    mcc_thresholds,
    merchant_mcc_map,
    min_charges,
    charges,
)

from typing import List


def check_count(
    merchant_charges: dict,
    min_charges: int,
    merchant_fradulent_charges: dict,
    mcc_thresholds: dict,
    merchant_mccs: dict,
    mch: str,
    merchant_fraud_flag: dict,
):
    if merchant_fraud_flag[mch]:
        return
    total_chg = merchant_charges[mch] + merchant_fradulent_charges[mch]
    if total_chg < min_charges:
        return
    mcc = merchant_mccs[mch]
    threshold = mcc_thresholds[mcc]
    if merchant_fradulent_charges[mch] >= threshold:
        merchant_fraud_flag[mch] = True


def check_ratio(
    merchant_charges: dict,
    min_charges: int,
    merchant_fradulent_charges: dict,
    mcc_thresholds: dict,
    merchant_mccs: dict,
    mch: str,
    merchant_fraud_flag: dict,
):
    if merchant_fraud_flag[mch]:
        return
    total_chg = merchant_charges[mch] + merchant_fradulent_charges[mch]
    if total_chg < min_charges:
        return
    mcc = merchant_mccs[mch]
    threshold = mcc_thresholds[mcc]
    ratio = float(merchant_fradulent_charges[mch]) / float(total_chg)
    if ratio >= threshold:
        merchant_fraud_flag[mch] = True


def check_dispute(
    merchant_charges: dict,
    min_charges: int,
    merchant_fradulent_charges: dict,
    mcc_thresholds: dict,
    merchant_mccs: dict,
    mch: str,
    merchant_fraud_flag: dict,
    calc_mode: str,
    chg_track: dict[str],
    chg_id: str,
):
    mch = chg_track[chg_id]
    merchant_charges[mch] += 1
    merchant_fradulent_charges[mch] -= 1
    # we recalculate the count and ratio to revert if needed
    total_chg = merchant_charges[mch] + merchant_fradulent_charges[mch]
    if total_chg < min_charges:
        return
    mcc = merchant_mccs[mch]
    threshold = mcc_thresholds[mcc]
    if calc_mode == "count":
        if merchant_fradulent_charges[mch] >= threshold:
            merchant_fraud_flag[mch] = True
            return
        else:
            merchant_fraud_flag[mch] = False
    elif calc_mode == "ratio":
        ratio = float(merchant_fradulent_charges[mch]) / float(total_chg)
        if ratio >= threshold:
            merchant_fraud_flag[mch] = True
            return
        else:
            merchant_fraud_flag[mch] = False
    else:
        raise Exception("Unrecognized calc_mode")


def process_chg(
    chg_type: str,
    chg_id: str,
    act_id: str,
    amt: str,
    code: str,
    merchant_charges: dict,
    merchant_fradulent_charges: dict,
    fraud_codes: dict,
    non_fraud_codes: dict,
    min_charges: int,
    merchant_fraud_flag: dict,
    merchant_mccs: dict,
    mcc_thresholds: dict,
    calc_mode: str,
    chg_track: dict[str],
):
    if chg_type == "CHARGE":
        if fraud_codes.get(code):
            merchant_fradulent_charges[act_id] += 1
        elif non_fraud_codes.get(code):
            merchant_charges[act_id] += 1
        else:
            raise Exception("Undetected code")

        if calc_mode == "count":
            check_count(
                merchant_charges=merchant_charges,
                min_charges=min_charges,
                merchant_fradulent_charges=merchant_fradulent_charges,
                mcc_thresholds=mcc_thresholds,
                mch=act_id,
                merchant_fraud_flag=merchant_fraud_flag,
                merchant_mccs=merchant_mccs,
            )
        elif calc_mode == "ratio":
            check_ratio(
                merchant_charges=merchant_charges,
                min_charges=min_charges,
                merchant_fradulent_charges=merchant_fradulent_charges,
                mcc_thresholds=mcc_thresholds,
                mch=act_id,
                merchant_fraud_flag=merchant_fraud_flag,
                merchant_mccs=merchant_mccs,
            )
        else:
            raise Exception("Calc mode not recognized")
        pass
    elif chg_type == "DISPUTE":
        # a disputed charge is treated as non-fradulent
        # merchant_charges[act_id] += 1
        check_dispute(
            merchant_charges=merchant_charges,
            min_charges=min_charges,
            merchant_fradulent_charges=merchant_fradulent_charges,
            mcc_thresholds=mcc_thresholds,
            mch=act_id,
            merchant_fraud_flag=merchant_fraud_flag,
            merchant_mccs=merchant_mccs,
            calc_mode=calc_mode,
            chg_track=chg_track,
            chg_id=chg_id,
        )
        pass
    else:
        raise Exception("Non-existent chg_type")


def find_fraudulent_merchants(
    non_fraud_codes: str,
    fraud_codes: str,
    mcc_thresholds: List[str],
    merchant_mcc_map: List[str],
    min_charges: str,
    charges: List[str],
) -> str:
    # -----------------------------
    # Your implementation here
    # -----------------------------
    # first extract the merchants, it is in input 4
    _merchant_scores = defaultdict(int)  # initialie with 1
    _merchant_mccs = defaultdict(str)
    _merchant_charges = defaultdict(int)
    _merchant_fradulent_charges = defaultdict(int)
    _mcc_threshold = defaultdict(int)
    _fraud_codes = defaultdict(lambda: 1)
    _non_fraud_codes = defaultdict(lambda: 1)
    _merchant_fraud_flag = defaultdict(lambda: False)
    _chg_track = defaultdict(str)

    for code in non_fraud_codes.split(","):
        _non_fraud_codes[code.strip()] = 1
    for code in fraud_codes.split(","):
        _fraud_codes[code.strip()] = 1

    for info in merchant_mcc_map:
        mch, mcc = info.split(",")
        _merchant_scores[mch] = 0
        _merchant_mccs[mch] = mcc
        _merchant_charges[mch] = 0

    calc_mode = "ratio"

    for info in mcc_thresholds:
        mcc, threshold = info.split(",")
        _mcc_threshold[mcc] = float(threshold)
        if float(threshold) >= 1:
            calc_mode = "count"

    # we can either charge or dispute
    for info in charges:
        chg_type = info.split(",")[0].strip()
        if chg_type == "CHARGE":
            chg_type, chg_id, act_id, amt, code = info.split(",")
            _chg_track[chg_id] = act_id
        else:
            chg_type, chg_id = info.split(",")
            act_id = None
            amt = None
            code = None
        process_chg(
            chg_type,
            chg_id,
            act_id,
            amt,
            code,
            _merchant_charges,
            _merchant_fradulent_charges,
            fraud_codes=_fraud_codes,
            non_fraud_codes=_non_fraud_codes,
            min_charges=int(min_charges),
            merchant_fraud_flag=_merchant_fraud_flag,
            merchant_mccs=_merchant_mccs,
            mcc_thresholds=_mcc_threshold,
            calc_mode=calc_mode,
            chg_track=_chg_track,
        )
    frauds = []

    for key in _merchant_fraud_flag.keys():
        if _merchant_fraud_flag[key]:
            frauds.append(key)

    print(",".join(sorted(frauds)))


find_fraudulent_merchants(
    non_fraud_codes, fraud_codes, mcc_thresholds, merchant_mcc_map, min_charges, charges
)
