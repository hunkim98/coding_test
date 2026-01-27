# Account Balance Manager

## Problem Description

You are building a transaction processing system for a bank. The system must track money moving between accounts, enforce overdraft rules, and handle platform coverage for shortfalls.

Complete the following three functions:

---

## Part 1: Get Account Balances

### Function Signature

```python
def get_account_balances(transactions: List[Dict]) -> Dict[str, int]:
```

### Description

Process a list of transactions and return the final balance for each account. Only include accounts with a **positive balance** in the result.

### Input Format

- `transactions`: A list of dictionaries, each containing:
  - `account_id` (string): The account identifier
  - `amount` (integer): Positive for deposits, negative for withdrawals

### Output Format

- Return a dictionary mapping `account_id` to final balance
- Only include accounts where balance > 0
- Accounts with zero or negative balance should be excluded

### Sample Input

```python
transactions = [
    {"account_id": "account_A", "amount": 100},
    {"account_id": "account_B", "amount": 50},
    {"account_id": "account_A", "amount": -30},
    {"account_id": "account_C", "amount": 200},
    {"account_id": "account_B", "amount": -50}
]
```

### Sample Output

```python
{"account_A": 70, "account_C": 200}
```

### Explanation

- `account_A`: 100 - 30 = 70 (positive, included)
- `account_B`: 50 - 50 = 0 (zero, excluded)
- `account_C`: 200 (positive, included)

### Constraints

- 0 ≤ len(transactions) ≤ 10^5
- Account IDs are non-empty strings
- Amounts are integers in range [-10^9, 10^9]

---

## Part 2: Process Transactions (Overdraft Protection)

### Function Signature

```python
def process_transactions(transactions: List[Dict]) -> Tuple[Dict[str, int], List[Dict]]:
```

### Description

Process transactions with overdraft protection. If a withdrawal would make the balance negative, **reject** the transaction. Return both the final balances and a list of rejected transactions.

### Input Format

Same as Part 1.

### Output Format

Return a tuple of two elements:
1. Dictionary of final balances (include accounts with zero balance)
2. List of rejected transactions in the order they were rejected

### Sample Input

```python
transactions = [
    {"account_id": "account_A", "amount": 100},
    {"account_id": "account_A", "amount": -150},
    {"account_id": "account_B", "amount": 50},
    {"account_id": "account_A", "amount": -80},
    {"account_id": "account_B", "amount": -100}
]
```

### Sample Output

```python
(
    {"account_A": 20, "account_B": 50},
    [
        {"account_id": "account_A", "amount": -150},
        {"account_id": "account_B", "amount": -100}
    ]
)
```

### Explanation

1. `account_A` +100 → balance: 100 ✓
2. `account_A` -150 → would be -50 ✗ REJECTED
3. `account_B` +50 → balance: 50 ✓
4. `account_A` -80 → balance: 20 ✓
5. `account_B` -100 → would be -50 ✗ REJECTED

### Rules

- Process transactions in order
- Deposits (positive amounts) are always accepted
- Withdrawals that would result in negative balance are rejected
- Rejected transactions do not affect the balance
- Include accounts with zero balance in the result

---

## Part 3: Process with Platform Coverage

### Function Signature

```python
def process_with_coverage(transactions: List[Dict], platform_account_id: str) -> int:
```

### Description

Instead of rejecting overdrafts, the platform account covers the shortfall. When a transaction would make a user's balance negative:
1. The platform account pays the difference
2. The user's account is set to exactly 0
3. The transaction is still processed

Return the **total amount** the platform had to cover.

### Input Format

- `transactions`: Same as Part 1
- `platform_account_id`: The ID of the platform account that covers shortfalls

### Output Format

- Return an integer: the total coverage amount paid by the platform

### Sample Input

```python
transactions = [
    {"account_id": "platform", "amount": 1000},
    {"account_id": "account_A", "amount": 100},
    {"account_id": "account_A", "amount": -150},
    {"account_id": "account_B", "amount": 50},
    {"account_id": "account_B", "amount": -100},
    {"account_id": "account_A", "amount": -30}
]
platform_account_id = "platform"
```

### Sample Output

```python
130
```

### Explanation

1. `platform` +1000 → platform: 1000
2. `account_A` +100 → account_A: 100
3. `account_A` -150 → would be -50, platform covers 50 → account_A: 0, platform: 950
4. `account_B` +50 → account_B: 50
5. `account_B` -100 → would be -50, platform covers 50 → account_B: 0, platform: 900
6. `account_A` -30 → would be -30, platform covers 30 → account_A: 0, platform: 870

Total coverage: 50 + 50 + 30 = **130**

### Rules

- The platform account behaves normally for its own transactions
- Only cover shortfalls for non-platform accounts
- Coverage = absolute value of the negative balance that would result
- After coverage, the user's balance becomes exactly 0
- Assume the platform always has sufficient funds

---

## Constraints (All Parts)

- 0 ≤ len(transactions) ≤ 10^5
- Account IDs are non-empty strings containing only alphanumeric characters and underscores
- Amounts are integers in range [-10^9, 10^9]
- All accounts start with a balance of 0

---

## Notes

- Process all transactions in the order they appear in the list
- An account does not need to be initialized before receiving transactions
- Each part builds on the concepts from previous parts, but implement them as separate functions
