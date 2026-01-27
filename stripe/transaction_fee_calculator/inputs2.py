# Part 2: Conditional Fee Rules
# Status checks and regional rates

part = 2

# Test case 1: Mixed statuses and Ireland rates
csv_data_1 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
py_1,1,1000,eur,2024-12-24,acct_1,ie,payment,card,payment_completed
py_2,2,2500,eur,2024-12-24,acct_2,de,payment,card,payment_failed
py_3,3,3400,eur,2024-12-25,acct_2,ie,payment,klarna,payment_completed
py_4,4,5000,eur,2024-12-25,acct_1,fr,payment,bank_transfer,payment_completed
py_5,5,2000,eur,2024-12-26,acct_1,ie,payment,card,payment_pending"""

# py_1: Ireland card: 1000 × 0.019 + 20 = 39
# py_2: Failed -> 0
# py_3: Ireland klarna: 3400 × 0.025 + 40 = 125
# py_4: France standard: 5000 × 0.008 = 40
# py_5: Pending -> 0
expected_1 = """id,transaction_type,payment_provider,fee
py_1,payment,card,39
py_2,payment,card,0
py_3,payment,klarna,125
py_4,payment,bank_transfer,40
py_5,payment,card,0"""

# Test case 2: All Ireland transactions
csv_data_2 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
ie_1,1,1000,eur,2024-01-01,acct_1,ie,payment,card,payment_completed
ie_2,2,2000,eur,2024-01-01,acct_1,ie,payment,klarna,payment_completed
ie_3,3,5000,eur,2024-01-02,acct_1,ie,payment,bank_transfer,payment_completed"""

# ie_1: 1000 × 0.019 + 20 = 39
# ie_2: 2000 × 0.025 + 40 = 90
# ie_3: 5000 × 0.008 = 40 (bank_transfer same rate)
expected_2 = """id,transaction_type,payment_provider,fee
ie_1,payment,card,39
ie_2,payment,klarna,90
ie_3,payment,bank_transfer,40"""

# Test case 3: All failed transactions
csv_data_3 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
f_1,1,10000,usd,2024-02-01,acct_2,us,payment,card,payment_failed
f_2,2,5000,usd,2024-02-01,acct_2,us,payment,klarna,payment_failed
f_3,3,20000,usd,2024-02-02,acct_2,us,payment,bank_transfer,payment_declined"""

# All failed -> 0
expected_3 = """id,transaction_type,payment_provider,fee
f_1,payment,card,0
f_2,payment,klarna,0
f_3,payment,bank_transfer,0"""

# Test case 4: Compare Ireland vs standard rates
csv_data_4 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
cmp_1,1,5000,eur,2024-03-01,acct_3,ie,payment,card,payment_completed
cmp_2,2,5000,eur,2024-03-01,acct_3,de,payment,card,payment_completed
cmp_3,3,5000,eur,2024-03-01,acct_3,ie,payment,klarna,payment_completed
cmp_4,4,5000,eur,2024-03-01,acct_3,de,payment,klarna,payment_completed"""

# cmp_1: Ireland card: 5000 × 0.019 + 20 = 115
# cmp_2: Standard card: 5000 × 0.029 + 30 = 175
# cmp_3: Ireland klarna: 5000 × 0.025 + 40 = 165
# cmp_4: Standard klarna: 5000 × 0.035 + 50 = 225
expected_4 = """id,transaction_type,payment_provider,fee
cmp_1,payment,card,115
cmp_2,payment,card,175
cmp_3,payment,klarna,165
cmp_4,payment,klarna,225"""

test_cases = [
    {"csv_data": csv_data_1, "expected": expected_1},
    {"csv_data": csv_data_2, "expected": expected_2},
    {"csv_data": csv_data_3, "expected": expected_3},
    {"csv_data": csv_data_4, "expected": expected_4},
]
