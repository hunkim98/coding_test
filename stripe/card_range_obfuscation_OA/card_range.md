# Card Range Obfuscation (BIN Gap Filling)

## Background

Payment card numbers consist of 8 to 19 digits, with the first six digits referred to as
the Bank Identification Number (BIN). Stripe's card metadata API provides information about
different card brands within each BIN range by returning mappings of card intervals to brands.

However, a given BIN range might have gaps (at the beginning, middle, or end), where no valid
card numbers are present. Fraudsters may exploit these gaps to test for valid card numbers,
leading to a high probability of fraud. To prevent this, the missing intervals need to be
filled, ensuring the entire range is covered.

NOTE: Though the question is split into parts to guide your implementation, there are test
cases for all three parts, so your solution should work for all three parts.

---

## Terminology

- **BIN Range**: All 16-digit card numbers starting with a specific BIN. For example, a BIN
  of 424242 represents the range 4242420000000000 to 4242429999999999 (inclusive).
- **Interval**: A subset of the BIN range, inclusive of its start and end values.

## Inputs

- `bin_number`: A 6-digit string (e.g., "424242")
- `intervals`: A list of strings, each formatted as "start,end,brand"
  - start and end are 16-digit card numbers (inclusive)
  - brand is a string like "visa", "mastercard", etc.

## Output

A list of strings in the same format "start,end,brand", sorted by start value, covering the
entire BIN range with no gaps and no overlaps. Filled gaps should use the brand name "unknown".

---

## Part 1: Basic Gap Filling

Input intervals are already sorted by start value and do not overlap.

Your task: Fill in gaps at the beginning, middle, and end of the BIN range with "unknown" brand.

### Computing the BIN range

- Range start: `BIN * 10^10` (e.g., 424242 * 10^10 = 4242420000000000)
- Range end: `BIN * 10^10 + 10^10 - 1` (e.g., 4242429999999999)

### Example

BIN: 424242
Intervals:
  4242420500000000,4242421000000000,visa
  4242425000000000,4242428000000000,mastercard

Output:
  4242420000000000,4242420499999999,unknown
  4242420500000000,4242421000000000,visa
  4242421000000001,4242424999999999,unknown
  4242425000000000,4242428000000000,mastercard
  4242428000000001,4242429999999999,unknown

---

## Part 2: Unsorted Input + Merging

Input intervals may now be unsorted, and there may be overlapping or adjacent intervals
with the same brand that should be merged.

Rules:
- Sort intervals by start value first
- Merge overlapping or adjacent intervals that have the same brand
- Adjacent means interval A's end + 1 == interval B's start
- Different brands are never merged even if adjacent
- After merging, fill gaps as in Part 1

### Example

BIN: 424242
Intervals:
  4242425000000000,4242429999999999,visa
  4242420000000000,4242424999999999,visa

Output:
  4242420000000000,4242429999999999,visa

---

## Part 3: Edge Cases

Handle these edge cases:
- Empty interval list (entire range becomes "unknown")
- Full coverage (no gaps to fill)
- Single card number intervals (start == end)
- Different BIN numbers

### Example

BIN: 424242
Intervals: (empty)

Output:
  4242420000000000,4242429999999999,unknown

---

## Function Signature (Python)

```python
from typing import List

def fill_bin_gaps(bin_number: str, intervals: List[str]) -> List[str]:
    pass
```
