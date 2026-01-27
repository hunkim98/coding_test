# Phase 4: Any Path Length
# Graph traversal with any number of intermediate currencies
#
# Expected output for getRate("USD", "AUD"):
# Path: USD→EUR→GBP→JPY→AUD
# Rate: 0.85 × 0.88 × 150 × 0.012 = 1.3464
# Returns: 1.3464

phase = 4

rates = "USD:EUR:0.85,EUR:GBP:0.88,GBP:JPY:150,JPY:AUD:0.012"

test_cases = [
    ("USD", "AUD", 1.3464),    # USD→EUR→GBP→JPY→AUD
    ("AUD", "USD", 0.7427007299270073),  # 1/1.3464
    ("USD", "JPY", 112.2),     # USD→EUR→GBP→JPY = 0.85 × 0.88 × 150
    ("EUR", "AUD", 1.584),     # EUR→GBP→JPY→AUD = 0.88 × 150 × 0.012
    ("USD", "CHF", None),      # CHF not in graph
]

# Additional test with multiple paths
rates_complex = "USD:EUR:0.9,USD:GBP:0.8,EUR:GBP:0.85,GBP:CHF:1.2,EUR:CHF:1.1,CHF:JPY:120"

test_cases_complex = [
    # Multiple paths to JPY, find the best
    ("USD", "JPY", None),  # Calculate manually and add expected value
]
