"""
Card Range Obfuscation (BIN Gap Filling)

Parts:
- Part 1: Basic gap filling (sorted input, no overlaps)
- Part 2: Unsorted input + merge overlapping/adjacent same-brand intervals
- Part 3: Edge cases (empty, full coverage, single card, different BINs)
"""

from typing import List
from inputs3 import test_cases, part


def fill_bin_gaps(bin_number: str, intervals: List[str]) -> List[str]:
    """
    Given a 6-digit BIN and a list of intervals (start,end,brand),
    return a sorted list of intervals covering the entire BIN range
    with gaps filled using "unknown" brand.

    BIN range for 16-digit cards:
      start = BIN * 10^10
      end   = BIN * 10^10 + 10^10 - 1
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    start = int(bin_number) * 10**10

    merged = []
    brand = None
    brand_start = None
    brand_end = None
    intervals.sort()
    for item in intervals:
        # we have to check overlapping
        args = item.split(",")
        item_start = int(args[0])
        item_end = int(args[1])
        item_brand = args[2]
        if brand != item_brand:
            if brand is not None:
                merged.append(f"{brand_start},{brand_end},{brand}")
            brand_start = item_start
            brand_end = item_end
            brand = item_brand
        else:
            brand_end = item_end
    merged.append(f"{brand_start},{brand_end},{brand}")

    end = start
    result = []
    brand = "unknown"

    for item in merged:
        args = item.split(",")
        if not args[0].isdigit():
            break
        item_start = int(args[0])
        item_end = int(args[1])
        if end < item_start:
            result.append(f"{end},{item_start - 1},unknown")
        brand = args[2]
        result.append(f"{item_start},{item_end},{brand}")
        end = item_end + 1
    last = int(bin_number) * 10**10 + 10**10 - 1
    if end < last:
        result.append(f"{end},{last},unknown")

    return result


def run_tests():
    print(f"Testing Part {part}")
    for i, tc in enumerate(test_cases):
        result = fill_bin_gaps(tc["bin"], tc["intervals"])
        passed = result == tc["expected"]
        status = "PASS" if passed else "FAIL"
        print(f"  {status}: Test {i + 1}")
        if not passed:
            print(f"    Expected: {tc['expected']}")
            print(f"    Got:      {result}")


if __name__ == "__main__":
    run_tests()
