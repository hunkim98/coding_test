# Part 3: Covering Negative Balances
# Expected output: 130 (total coverage by platform)

part = 3

transactions = [
    {"account_id": "platform", "amount": 1000},
    {"account_id": "account_A", "amount": 100},
    {"account_id": "account_A", "amount": -150},  # Needs 50 from platform
    {"account_id": "account_B", "amount": 50},
    {"account_id": "account_B", "amount": -100},  # Needs 50 from platform
    {"account_id": "account_A", "amount": -30}    # Needs 30 from platform
]

platform_account_id = "platform"
