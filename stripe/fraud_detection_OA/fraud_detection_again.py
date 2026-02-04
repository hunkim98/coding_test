from collections import defaultdict
from operator import is_
from inputs3 import (
    non_fraud_codes,
    fraud_codes,
    mcc_thresholds,
    merchant_mcc_map,
    min_charges,
    charges,
)

from typing import List


def find_fraudulent_merchants(
    non_fraud_codes: str,
    fraud_codes: str,
    mcc_thresholds: List[str],
    merchant_mcc_map: List[str],
    min_charges: str,
    charges: List[str],
) -> str:
    _mcc_thr = {}
    _min_charges_req = int(min_charges)
    is_ratio = False

    for item in mcc_thresholds:
        args = item.split(",")
        mcc = args[0].strip()
        thr = args[1].strip()
        if "." in thr or is_ratio:
            is_ratio = True
        _mcc_thr[mcc] = float(thr)
    _mid_mcc = {}
    _mid_total = defaultdict(int)
    _mid_fraud = defaultdict(int)
    _cid_disputed = {}
    _mid_dispute = defaultdict(int)
    for item in merchant_mcc_map:
        args = item.split(",")
        mid = args[0].strip()
        mcc = args[1].strip()
        _mid_mcc[mid] = mcc

    for item in charges:
        args = item.split(",")
        tr_type = args[0].strip()
        cid = args[1].strip()
        if tr_type != "CHARGE":
            if _cid_disputed.get(cid) is not None:
                _cid_disputed[cid] = True
                _mid_dispute[mid] += 1
                _mid_fraud[mid] -= 1
            continue
        mid = args[2].strip()
        amt = int(args[3].strip())
        code = args[4].strip()
        _mid_total[mid] += 1
        if code in fraud_codes:
            _mid_fraud[mid] += 1
            pass
        _cid_disputed[cid] = False
        # if tr_type == "CHARGE":
        #     cnt_threshold(
        #         non_fraud_codes=non_fraud_codes,
        #         fraud_codes=fraud_codes,
        #         min_charges_req=_min_charges_req,
        #         mid=mid,
        #         amt=amt,
        #         code=code,
        #         _mcc_thr=_mcc_thr,
        #     )
    # check threshold
    result = set()
    for mid in _mid_total.keys():
        total_charges = _mid_total[mid]
        if total_charges < _min_charges_req:
            continue
        fraud_charges = _mid_fraud[mid]
        mid_mcc = _mid_mcc[mid]
        mid_thr = _mcc_thr[mid_mcc]

        if not is_ratio:
            if fraud_charges >= mid_thr:
                result.add(mid)
        else:
            if fraud_charges / total_charges >= mid_thr:
                result.add(mid)

    print(",".join(sorted(result)))
    return sorted(result)


find_fraudulent_merchants(
    non_fraud_codes, fraud_codes, mcc_thresholds, merchant_mcc_map, min_charges, charges
)
