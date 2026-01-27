# Payment Reconciliation

## Problem Description

You are building a system that processes payment data and reconciles it with bank transactions. This involves parsing payment JSON files, converting them to a fixed-width clearing file format, and matching them against bank records.

This is a 4-part problem testing JSON parsing, string formatting, and data matching skills.

---

## Input Formats

### Payment Intent JSON

```json
[
  {"merchant": "acct_707", "amt": 91088, "currency": "usd"},
  {"merchant": "acct_707", "amt": 77855, "currency": "usd"}
]
```

- `merchant`: Account identifier
- `amt`: Amount in minor units (cents for USD)
- `currency`: 3-letter ISO currency code (lowercase)

### Clearing File Format (Fixed-Width)

Each line has comma-separated fixed-width columns:

| Column | Name | Width | Format |
|--------|------|-------|--------|
| 1 | ARN | 22 bytes | Digits 0-9 (unique ID) |
| 2 | Timestamp | 20 bytes | Digits 0-9 (Unix epoch ms) |
| 3 | Amount | 10 bytes | Digits 0-9 (zero-padded) |
| 4 | Currency | 3 bytes | Lowercase letters |

**Example:**
```
0000000000000000000001,00000001704067200000,0000091088,usd
0000000000000000000002,00000001704067200001,0000077855,usd
```

### Bank Account Transaction Format

| Column | Name | Width | Format |
|--------|------|-------|--------|
| 1 | Transaction ID | 8 bytes | Hex (0-9, A-F) |
| 2 | Timestamp | 20 bytes | Unix epoch ms |
| 3 | Amount | 10 bytes | Zero-padded |
| 4 | Currency | 3 bytes | Lowercase |

### Reconciliation Report Format

| Column | Name | Width | Format |
|--------|------|-------|--------|
| 1 | ARN | 22 bytes | Digits |
| 2 | Status | 7 bytes | PENDING/SETTLED/DISPUTE |
| 3 | Bank Transaction ID | 8 bytes | Hex or zeros |

---

## Part 1: Parse Payment JSON

### Description

Read payment JSON files and extract summary statistics.

### Function Signature

```python
def parse_payments(json_file: str) -> dict:
    """
    Returns: {
        "count": int,           # Number of transactions
        "total": int,           # Sum of all amounts
        "by_merchant": dict,    # {merchant_id: total_amount}
        "by_currency": dict     # {currency: total_amount}
    }
    """
```

### Sample Input

```json
[
  {"merchant": "acct_707", "amt": 91088, "currency": "usd"},
  {"merchant": "acct_707", "amt": 77855, "currency": "usd"},
  {"merchant": "acct_732", "amt": 50000, "currency": "eur"}
]
```

### Sample Output

```python
{
    "count": 3,
    "total": 218943,
    "by_merchant": {"acct_707": 168943, "acct_732": 50000},
    "by_currency": {"usd": 168943, "eur": 50000}
}
```

---

## Part 2: Generate Clearing File

### Description

Convert payment data to fixed-width clearing file format.

### Function Signature

```python
def generate_clearing_file(payments: List[dict], start_timestamp: int = 1704067200000) -> str:
    """
    Args:
        payments: List of payment dicts
        start_timestamp: Base timestamp (increment by 1 for each payment)

    Returns:
        Clearing file as string (newline-separated rows)
    """
```

### Sample Input

```python
payments = [
    {"merchant": "acct_707", "amt": 91088, "currency": "usd"},
    {"merchant": "acct_707", "amt": 77855, "currency": "usd"}
]
```

### Sample Output

```
0000000000000000000001,00000001704067200000,0000091088,usd
0000000000000000000002,00000001704067200001,0000077855,usd
```

### Rules

- ARN: Sequential, starting from 1, zero-padded to 22 digits
- Timestamp: Zero-padded to 20 digits, increment by 1 for each row
- Amount: Zero-padded to 10 digits
- Currency: 3 lowercase letters

---

## Part 3: Reconciliation

### Description

Match clearing file entries against bank transactions to determine status.

### Function Signature

```python
def reconcile(clearing_entries: List[str], bank_transactions: List[str]) -> str:
    """
    Args:
        clearing_entries: List of clearing file lines
        bank_transactions: List of bank transaction lines

    Returns:
        Reconciliation report as string
    """
```

### Matching Rules

- Match by **amount** and **currency**
- Bank timestamp must be >= clearing timestamp
- Each bank transaction can settle multiple clearing entries
- Mark as SETTLED if matched, PENDING if not

### Sample Input

```python
clearing_entries = [
    "0000000000000000000001,00000001704067200000,0000091088,usd",
    "0000000000000000000002,00000001704067200001,0000077855,usd"
]

bank_transactions = [
    "A1B2C3D4,00000001704067300000,0000168943,usd"  # 91088 + 77855 = 168943
]
```

### Sample Output

```
0000000000000000000001,SETTLED,A1B2C3D4
0000000000000000000002,SETTLED,A1B2C3D4
```

---

## Part 4: Handle Disputes

### Description

Add dispute handling to the reconciliation logic.

### Dispute Format

| Column | Name | Width |
|--------|------|-------|
| 1 | Bank Transaction ID | 8 bytes |
| 2 | ARN | 22 bytes |
| 3 | Amount | 10 bytes |
| 4 | Currency | 3 bytes |

### Function Signature

```python
def reconcile_with_disputes(
    clearing_entries: List[str],
    bank_transactions: List[str],
    disputes: List[str]
) -> str:
```

### Rules

- If an ARN appears in disputes, mark as DISPUTE instead of SETTLED
- Disputed amounts are deducted from the settlement

---

## Constraints

- Amount values: 0 to 10^9
- ARN: Unique per clearing file
- Timestamps: Valid Unix epoch milliseconds
- Currency: Valid 3-letter ISO code

---

## Notes

- Focus on clean, maintainable code
- Handle edge cases (empty files, missing data)
- Fixed-width formatting must be exact
- This is a data transformation problem, not algorithm optimization
