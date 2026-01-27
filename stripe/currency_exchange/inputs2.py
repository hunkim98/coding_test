# Phase 2: One-Step Connection
# Expected outputs:
# getRate("USD", "GBP") = 0.748 (0.85 × 0.88, via EUR)
# getRate("GBP", "USD") = 1.3368... (1/0.748)
# getRate("JPY", "EUR") = 0.00772... (1/110 × 0.85, via USD)

phase = 2

rates = "USD:EUR:0.85,EUR:GBP:0.88,USD:JPY:110"

test_cases = [
    # Direct rates still work
    ("USD", "EUR", 0.85),
    ("EUR", "USD", 1.1764705882352942),

    # One-step connections
    ("USD", "GBP", 0.748),           # USD→EUR→GBP
    ("GBP", "USD", 1.3368983957219252),  # GBP→EUR→USD
    ("JPY", "GBP", 0.0068),          # JPY→USD→EUR→GBP (needs 2 steps - may be None)
    ("EUR", "JPY", 129.41176470588235),  # EUR→USD→JPY
]
