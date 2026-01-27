# Phase 1: Direct Rates
# Expected outputs:
# getRate("USD", "EUR") = 0.85
# getRate("EUR", "USD") = 1.1764705882352942 (1/0.85)
# getRate("USD", "USD") = 1.0
# getRate("USD", "GBP") = None (no direct link)

phase = 1

rates = "USD:EUR:0.85,EUR:GBP:0.88,USD:JPY:110"

test_cases = [
    ("USD", "EUR", 0.85),
    ("EUR", "USD", 1.1764705882352942),
    ("USD", "USD", 1.0),
    ("EUR", "GBP", 0.88),
    ("GBP", "EUR", 1.1363636363636365),
    ("USD", "GBP", None),  # No direct link
    ("GBP", "JPY", None),  # No direct link
]
