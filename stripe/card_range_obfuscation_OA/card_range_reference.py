"""
Card Range Obfuscation - Reference solution.

Algorithm: Sort -> Merge same-brand adjacent/overlapping -> Fill gaps
Time: O(N log N)
"""
from typing import List


def fill_bin_gaps(bin_number: str, intervals: List[str]) -> List[str]:
    BIN = int(bin_number)
    lo = BIN * 10**10
    hi = lo + 10**10 - 1

    # Parse & sort
    parsed = []
    for iv in intervals:
        s, e, brand = iv.split(",")[0], iv.split(",")[1], iv.split(",")[2]
        parsed.append((int(s), int(e), brand))
    parsed.sort()

    # Merge overlapping/adjacent with same brand
    merged = []
    for s, e, b in parsed:
        if merged and merged[-1][2] == b and s <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e), b)
        else:
            merged.append((s, e, b))

    # Fill gaps
    result = []
    cur = lo
    for s, e, b in merged:
        if cur < s:
            result.append((cur, s - 1, "unknown"))
        result.append((s, e, b))
        cur = e + 1
    if cur <= hi:
        result.append((cur, hi, "unknown"))

    return [f"{s},{e},{b}" for s, e, b in result]


# Test runner
if __name__ == "__main__":
    from inputs1 import test_cases as t1, part as p1
    from inputs2 import test_cases as t2, part as p2
    from inputs3 import test_cases as t3, part as p3

    all_tests = [(p1, t1), (p2, t2), (p3, t3)]

    for part, tests in all_tests:
        print(f"Part {part}:")
        for i, tc in enumerate(tests):
            result = fill_bin_gaps(tc["bin"], tc["intervals"])
            passed = result == tc["expected"]
            status = "PASS" if passed else "FAIL"
            print(f"  {status}: Test {i + 1}")
            if not passed:
                print(f"    Expected: {tc['expected']}")
                print(f"    Got:      {result}")
    print("\nDone!")
