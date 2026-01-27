# Part 3: Volume-Based Discounts
# Discounts based on merchant transaction count

part = 3

# Country fees configuration (used for all test cases)
country_fees = {
    "ie": {"card": (0.019, 20), "klarna": (0.025, 40), "bank_transfer": (0.006, 0)},
    "de": {"card": (0.025, 25), "klarna": (0.030, 45), "bank_transfer": (0.007, 0)},
    "fr": {"card": (0.027, 28), "klarna": (0.032, 48), "bank_transfer": (0.008, 0)},
    "default": {"card": (0.029, 30), "klarna": (0.035, 50), "bank_transfer": (0.008, 0)}
}

# Test case 1: Simple volume discount crossing threshold
# Generate 10 transactions, then 11th gets 10% off
csv_lines_1 = ["id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status"]
for i in range(1, 13):
    csv_lines_1.append(f"tx_{i},{i},1000,eur,2024-01-01,acct_1,ie,payment,card,payment_completed")
csv_data_1 = "\n".join(csv_lines_1)

# Ireland card: 1000 × 0.019 + 20 = 39
# Transactions 1-10: No discount -> 39
# Transaction 11-12: 10% off -> 39 × 0.9 = 35.1 -> 35
expected_lines_1 = ["id,transaction_type,payment_provider,fee"]
for i in range(1, 11):
    expected_lines_1.append(f"tx_{i},payment,card,39")
for i in range(11, 13):
    expected_lines_1.append(f"tx_{i},payment,card,35")
expected_1 = "\n".join(expected_lines_1)

# Test case 2: Failed transactions don't count
csv_data_2 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
tx_1,1,1000,eur,2024-01-01,acct_2,ie,payment,card,payment_completed
tx_2,2,1000,eur,2024-01-01,acct_2,ie,payment,card,payment_failed
tx_3,3,1000,eur,2024-01-01,acct_2,ie,payment,card,payment_completed
tx_4,4,1000,eur,2024-01-01,acct_2,ie,payment,card,payment_failed"""

# tx_1: count=1, no discount -> 39
# tx_2: failed -> 0 (count stays 1)
# tx_3: count=2, no discount -> 39
# tx_4: failed -> 0
expected_2 = """id,transaction_type,payment_provider,fee
tx_1,payment,card,39
tx_2,payment,card,0
tx_3,payment,card,39
tx_4,payment,card,0"""

# Test case 3: Different countries use different rates
csv_data_3 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
tx_1,1,2000,eur,2024-01-01,acct_3,ie,payment,card,payment_completed
tx_2,2,2000,eur,2024-01-01,acct_3,de,payment,card,payment_completed
tx_3,3,2000,eur,2024-01-01,acct_3,fr,payment,card,payment_completed
tx_4,4,2000,usd,2024-01-01,acct_3,us,payment,card,payment_completed"""

# tx_1: Ireland: 2000 × 0.019 + 20 = 58, count=1
# tx_2: Germany: 2000 × 0.025 + 25 = 75, count=2
# tx_3: France: 2000 × 0.027 + 28 = 82, count=3
# tx_4: Default: 2000 × 0.029 + 30 = 88, count=4
expected_3 = """id,transaction_type,payment_provider,fee
tx_1,payment,card,58
tx_2,payment,card,75
tx_3,payment,card,82
tx_4,payment,card,88"""

# Test case 4: Multiple merchants independent counts
csv_data_4 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
tx_1,1,1000,eur,2024-01-01,acct_A,de,payment,card,payment_completed
tx_2,2,1000,eur,2024-01-01,acct_B,de,payment,card,payment_completed
tx_3,3,1000,eur,2024-01-01,acct_A,de,payment,card,payment_completed
tx_4,4,1000,eur,2024-01-01,acct_B,de,payment,card,payment_completed"""

# Germany card: 1000 × 0.025 + 25 = 50
# acct_A: tx_1 count=1, tx_3 count=2
# acct_B: tx_2 count=1, tx_4 count=2
# All under 10, no discounts
expected_4 = """id,transaction_type,payment_provider,fee
tx_1,payment,card,50
tx_2,payment,card,50
tx_3,payment,card,50
tx_4,payment,card,50"""

# Test case 5: Higher discount tiers
csv_lines_5 = ["id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status"]
for i in range(1, 55):
    csv_lines_5.append(f"tx_{i},{i},1000,eur,2024-01-01,acct_5,de,payment,card,payment_completed")
csv_data_5 = "\n".join(csv_lines_5)

# Germany card: 1000 × 0.025 + 25 = 50
# 1-10: no discount -> 50
# 11-50: 10% off -> 50 × 0.9 = 45
# 51-54: 15% off -> 50 × 0.85 = 42.5 -> 42
expected_lines_5 = ["id,transaction_type,payment_provider,fee"]
for i in range(1, 11):
    expected_lines_5.append(f"tx_{i},payment,card,50")
for i in range(11, 51):
    expected_lines_5.append(f"tx_{i},payment,card,45")
for i in range(51, 55):
    expected_lines_5.append(f"tx_{i},payment,card,42")
expected_5 = "\n".join(expected_lines_5)

test_cases = [
    {"csv_data": csv_data_1, "country_fees": country_fees, "expected": expected_1},
    {"csv_data": csv_data_2, "country_fees": country_fees, "expected": expected_2},
    {"csv_data": csv_data_3, "country_fees": country_fees, "expected": expected_3},
    {"csv_data": csv_data_4, "country_fees": country_fees, "expected": expected_4},
    {"csv_data": csv_data_5, "country_fees": country_fees, "expected": expected_5},
]
