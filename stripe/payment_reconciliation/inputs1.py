# Part 1: Parse Payment JSON
# Read JSON and extract summary statistics

part = 1

# Sample payment data (from fixture files)
payments_json_1 = """[
  {"merchant": "acct_707", "amt": 91088, "currency": "usd"},
  {"merchant": "acct_707", "amt": 77855, "currency": "usd"},
  {"merchant": "acct_707", "amt": 2732, "currency": "usd"},
  {"merchant": "acct_707", "amt": 24121, "currency": "usd"}
]"""

expected_1 = {
    "count": 4,
    "total": 195796,
    "by_merchant": {"acct_707": 195796},
    "by_currency": {"usd": 195796}
}

payments_json_2 = """[
  {"merchant": "acct_100", "amt": 50000, "currency": "usd"},
  {"merchant": "acct_100", "amt": 30000, "currency": "eur"},
  {"merchant": "acct_200", "amt": 25000, "currency": "usd"},
  {"merchant": "acct_200", "amt": 15000, "currency": "gbp"}
]"""

expected_2 = {
    "count": 4,
    "total": 120000,
    "by_merchant": {"acct_100": 80000, "acct_200": 40000},
    "by_currency": {"usd": 75000, "eur": 30000, "gbp": 15000}
}

test_cases = [
    {"json": payments_json_1, "expected": expected_1},
    {"json": payments_json_2, "expected": expected_2},
]
