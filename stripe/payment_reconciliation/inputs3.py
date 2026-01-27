# Part 3: Reconciliation
# Match clearing entries with bank transactions

part = 3

# Test case 1: All settled in one batch
clearing_1 = [
    "0000000000000000000001,00000001704067200000,0000091088,usd",
    "0000000000000000000002,00000001704067200001,0000077855,usd"
]

bank_transactions_1 = [
    "A1B2C3D4,00000001704067300000,0000168943,usd"  # 91088 + 77855 = 168943
]

expected_1 = """0000000000000000000001,SETTLED,A1B2C3D4
0000000000000000000002,SETTLED,A1B2C3D4"""

# Test case 2: Some pending, some settled
clearing_2 = [
    "0000000000000000000001,00000001704067200000,0000050000,usd",
    "0000000000000000000002,00000001704067200001,0000030000,usd",
    "0000000000000000000003,00000001704067200002,0000020000,eur"
]

bank_transactions_2 = [
    "DEADBEEF,00000001704067300000,0000080000,usd"  # Only USD settled
]

expected_2 = """0000000000000000000001,SETTLED,DEADBEEF
0000000000000000000002,SETTLED,DEADBEEF
0000000000000000000003,PENDING,00000000"""

# Test case 3: All pending (no bank transactions)
clearing_3 = [
    "0000000000000000000001,00000001704067200000,0000010000,usd"
]

bank_transactions_3 = []

expected_3 = """0000000000000000000001,PENDING,00000000"""

test_cases = [
    {"clearing": clearing_1, "bank": bank_transactions_1, "expected": expected_1},
    {"clearing": clearing_2, "bank": bank_transactions_2, "expected": expected_2},
    {"clearing": clearing_3, "bank": bank_transactions_3, "expected": expected_3},
]
