# Phase 3: Best Possible Rate
# Find the maximum rate among all paths
#
# Expected output for getRate("USD", "CAD"):
# Path 1: USD→GBP→CAD = 0.75 × 1.7 = 1.275 ← BEST
# Path 2: USD→EUR→CAD = 0.85 × 1.45 = 1.2325
# Path 3: USD→EUR→GBP→CAD = 0.85 × 0.88 × 1.7 = 1.2716
# Returns: 1.275

phase = 3

rates = "USD:EUR:0.85,USD:GBP:0.75,EUR:GBP:0.88,GBP:CAD:1.7,EUR:CAD:1.45"

test_cases = [
    ("USD", "CAD", 1.275),     # Best path: USD→GBP→CAD
    ("CAD", "USD", 0.7843137254901961),  # 1/1.275
    ("EUR", "CAD", 1.496),     # EUR→GBP→CAD = 0.88 × 1.7 = 1.496 (better than 1.45)
    ("USD", "EUR", 0.85),      # Direct rate
]
