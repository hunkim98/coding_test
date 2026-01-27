# Part 1: Basic Fee Calculation
# Calculate fees based on payment provider

part = 1

# Test case 1: Basic example
csv_data_1 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
py_1,1,1000,eur,2024-12-24,acct_1,ie,payment,card,payment_completed
py_2,2,2500,eur,2024-12-24,acct_2,de,payment,card,payment_failed
py_3,3,3400,eur,2024-12-25,acct_2,ie,payment,klarna,payment_completed
py_4,4,5000,eur,2024-12-25,acct_1,fr,payment,bank_transfer,payment_completed"""

# py_1: 1000 × 0.029 + 30 = 59
# py_2: 2500 × 0.029 + 30 = 102.5 -> 102
# py_3: 3400 × 0.035 + 50 = 169
# py_4: 5000 × 0.008 = 40
expected_1 = """id,transaction_type,payment_provider,fee
py_1,payment,card,59
py_2,payment,card,102
py_3,payment,klarna,169
py_4,payment,bank_transfer,40"""

# Test case 2: All card payments
csv_data_2 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
tx_1,1,500,usd,2024-01-01,acct_1,us,payment,card,payment_completed
tx_2,2,1500,usd,2024-01-01,acct_1,us,payment,card,payment_completed
tx_3,3,10000,usd,2024-01-02,acct_2,us,payment,card,payment_completed"""

# tx_1: 500 × 0.029 + 30 = 44.5 -> 44
# tx_2: 1500 × 0.029 + 30 = 73.5 -> 73
# tx_3: 10000 × 0.029 + 30 = 320
expected_2 = """id,transaction_type,payment_provider,fee
tx_1,payment,card,44
tx_2,payment,card,73
tx_3,payment,card,320"""

# Test case 3: All klarna payments
csv_data_3 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
k_1,1,2000,eur,2024-02-01,acct_3,de,payment,klarna,payment_completed
k_2,2,5000,eur,2024-02-02,acct_3,de,payment,klarna,payment_completed"""

# k_1: 2000 × 0.035 + 50 = 120
# k_2: 5000 × 0.035 + 50 = 225
expected_3 = """id,transaction_type,payment_provider,fee
k_1,payment,klarna,120
k_2,payment,klarna,225"""

# Test case 4: Bank transfers
csv_data_4 = """id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
bt_1,1,100000,usd,2024-03-01,acct_4,us,payment,bank_transfer,payment_completed
bt_2,2,50000,usd,2024-03-01,acct_4,us,payment,bank_transfer,payment_completed"""

# bt_1: 100000 × 0.008 = 800
# bt_2: 50000 × 0.008 = 400
expected_4 = """id,transaction_type,payment_provider,fee
bt_1,payment,bank_transfer,800
bt_2,payment,bank_transfer,400"""

test_cases = [
    {"csv_data": csv_data_1, "expected": expected_1},
    {"csv_data": csv_data_2, "expected": expected_2},
    {"csv_data": csv_data_3, "expected": expected_3},
    {"csv_data": csv_data_4, "expected": expected_4},
]
