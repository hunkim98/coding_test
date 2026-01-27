# Part 2: Stopping Overdrafts
# Expected output:
#   balances: {"account_A": 20, "account_B": 50}
#   rejected: [{"account_id": "account_A", "amount": -150}, {"account_id": "account_B", "amount": -100}]

part = 2

transactions = [
    {"account_id": "account_A", "amount": 100},
    {"account_id": "account_A", "amount": -150},  # Result is -50 -> REJECT
    {"account_id": "account_B", "amount": 50},
    {"account_id": "account_A", "amount": -80},   # Valid: 100 - 80 = 20
    {"account_id": "account_B", "amount": -100}   # Result is -50 -> REJECT
]
