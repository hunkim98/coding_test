# Transaction Fee Calculator

## Problem Description

Build a system that calculates fees for a payment platform. You receive transaction data as a CSV string and calculate fees based on specific rules.

---

## Input Data Format

CSV string with the following columns:

| Column | Description |
|--------|-------------|
| `id` | Unique transaction ID |
| `reference` | Reference number |
| `amount` | Amount in cents (1000 = $10.00) |
| `currency` | Currency code (e.g., "eur", "usd") |
| `date` | Transaction date (YYYY-MM-DD) |
| `merchant_id` | Seller's ID |
| `buyer_country` | Buyer's country code |
| `transaction_type` | Type of action (e.g., "payment") |
| `payment_provider` | Payment method (e.g., "card", "klarna") |
| `status` | Result (e.g., "payment_completed", "payment_failed") |

---

## Part 1: Basic Fee Calculation

### Task

Calculate fees for each transaction based on the payment provider.

### Fee Table

| Payment Provider | Fee Rate |
|-----------------|----------|
| card | 2.9% + 30 cents |
| klarna | 3.5% + 50 cents |
| bank_transfer | 0.8% flat |

### Formula

```
fee = amount × rate + fixed_fee
```

Round DOWN to nearest integer.

### Example

**Input:**
```
id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
py_1,1,1000,eur,2024-12-24,acct_1,ie,payment,card,payment_completed
py_2,2,2500,eur,2024-12-24,acct_2,de,payment,card,payment_failed
py_3,3,3400,eur,2024-12-25,acct_2,ie,payment,klarna,payment_completed
py_4,4,5000,eur,2024-12-25,acct_1,fr,payment,bank_transfer,payment_completed
```

**Output:**
```
id,transaction_type,payment_provider,fee
py_1,payment,card,59
py_2,payment,card,102
py_3,payment,klarna,169
py_4,payment,bank_transfer,40
```

**Calculations:**
- py_1: 1000 × 0.029 + 30 = 59
- py_2: 2500 × 0.029 + 30 = 102.5 → 102
- py_3: 3400 × 0.035 + 50 = 169
- py_4: 5000 × 0.008 = 40

---

## Part 2: Conditional Fee Rules

### New Rules

1. **Status Check**: Only charge fees for `payment_completed` status
2. **Failed/Pending**: Fee is 0
3. **Regional Rates**: Ireland ("ie") has special lower rates

### Ireland (ie) Special Rates

| Payment Provider | Fee Rate |
|-----------------|----------|
| card | 1.9% + 20 cents |
| klarna | 2.5% + 40 cents |
| bank_transfer | 0.8% flat (same) |

All other countries use standard rates from Part 1.

### Example

**Input:**
```
id,reference,amount,currency,date,merchant_id,buyer_country,transaction_type,payment_provider,status
py_1,1,1000,eur,2024-12-24,acct_1,ie,payment,card,payment_completed
py_2,2,2500,eur,2024-12-24,acct_2,de,payment,card,payment_failed
py_3,3,3400,eur,2024-12-25,acct_2,ie,payment,klarna,payment_completed
py_4,4,5000,eur,2024-12-25,acct_1,fr,payment,bank_transfer,payment_completed
py_5,5,2000,eur,2024-12-26,acct_1,ie,payment,card,payment_pending
```

**Output:**
```
id,transaction_type,payment_provider,fee
py_1,payment,card,39
py_2,payment,card,0
py_3,payment,klarna,125
py_4,payment,bank_transfer,40
py_5,payment,card,0
```

---

## Part 3: Volume-Based Discounts

### Task

Add volume discounts. Merchants with more successful transactions get lower fees.

### Discount Table

| Total Transactions (so far) | Discount |
|----------------------------|----------|
| 1-10 | 0% (Normal price) |
| 11-50 | 10% off |
| 51-100 | 15% off |
| 101+ | 20% off |

### Country Fee Configuration

```python
country_fees = {
    "ie": {"card": (0.019, 20), "klarna": (0.025, 40), "bank_transfer": (0.006, 0)},
    "de": {"card": (0.025, 25), "klarna": (0.030, 45), "bank_transfer": (0.007, 0)},
    "fr": {"card": (0.027, 28), "klarna": (0.032, 48), "bank_transfer": (0.008, 0)},
    "default": {"card": (0.029, 30), "klarna": (0.035, 50), "bank_transfer": (0.008, 0)}
}
```

### Rules

1. Count is checked **before** processing current transaction
2. Only **successful** transactions count toward volume
3. Process rows in CSV order
4. Apply discount to base fee, then round down

### Example Calculation

For merchant's 11th transaction (Ireland Card, amount 1500):
```
Base fee = 1500 × 0.019 + 20 = 48.5
Discount = 10%
Final fee = 48.5 × 0.9 = 43.65 → 43
```

---

## Output Format

CSV string with columns: `id,transaction_type,payment_provider,fee`

---

## Constraints

- Amounts are positive integers (cents)
- All transactions have valid payment providers
- Country codes are lowercase strings
- Process transactions in the order they appear

---

## Test Format

```python
# Part 1 & 2
def calculate_fees(csv_data: str) -> str:
    pass

# Part 3
def calculate_fees(csv_data: str, country_fees: dict) -> str:
    pass
```
