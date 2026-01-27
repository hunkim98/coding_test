# Part 2: Generate Clearing File
# Convert payment data to fixed-width format

part = 2

payments_1 = [
    {"merchant": "acct_707", "amt": 91088, "currency": "usd"},
    {"merchant": "acct_707", "amt": 77855, "currency": "usd"}
]

expected_1 = """0000000000000000000001,00000001704067200000,0000091088,usd
0000000000000000000002,00000001704067200001,0000077855,usd"""

payments_2 = [
    {"merchant": "acct_100", "amt": 123, "currency": "eur"},
    {"merchant": "acct_100", "amt": 9999999999, "currency": "usd"},
    {"merchant": "acct_200", "amt": 1, "currency": "gbp"}
]

expected_2 = """0000000000000000000001,00000001704067200000,0000000123,eur
0000000000000000000002,00000001704067200001,9999999999,usd
0000000000000000000003,00000001704067200002,0000000001,gbp"""

start_timestamp = 1704067200000  # 2024-01-01 00:00:00 UTC

test_cases = [
    {"payments": payments_1, "start_ts": start_timestamp, "expected": expected_1},
    {"payments": payments_2, "start_ts": start_timestamp, "expected": expected_2},
]
