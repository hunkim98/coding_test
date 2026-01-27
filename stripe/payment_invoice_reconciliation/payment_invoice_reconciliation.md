# Payment Invoice Reconciliation

## Problem Description

You are building a system that matches incoming payments to unpaid invoices. When a customer sends money, you must determine which invoice they are paying.

The matching logic has three priority levels:
1. **Match by ID**: Look for invoice ID in the payment memo
2. **Match by Amount**: If no ID, find invoice with exact amount (earliest date wins)
3. **Fuzzy Match**: If no exact amount, find invoice within tolerance range

---

## Input Format

**Payment** (string):
```
"payment-id, amount, memo"
```
- `payment-id`: Unique payment identifier
- `amount`: Payment amount in cents (integer)
- `memo`: Customer note (may contain invoice ID)

**Invoices** (list of strings):
```python
[
    "invoice-id, due-date, amount",
    "invoice-id, due-date, amount",
    ...
]
```
- `invoice-id`: Unique invoice identifier
- `due-date`: Date in YYYY-MM-DD format
- `amount`: Invoice amount in cents (integer)

---

## Output Format

**Match found:**
```
"Payment {payment-id} paid {amount} for invoice {invoice-id} due on {date}"
```

**No match:**
```
"Payment {payment-id} could not be matched to any invoice"
```

---

## Step 1: Match by ID

### Description

Extract invoice ID from the payment memo. Look for patterns like:
- "paying for: invoice-id"
- "Paying off: invoice-id"

Matching is case-insensitive for the pattern, but invoice IDs are case-sensitive.

### Function Signature

```python
def reconcile_payment(payment: str, invoices: List[str]) -> str:
```

### Sample Input/Output

```python
payment = "payment-001, 1000, Paying off: inv-123"
invoices = [
    "inv-123, 2024-03-15, 1000",
    "inv-456, 2024-03-20, 1000",
    "inv-789, 2024-02-10, 500"
]

# Returns: "Payment payment-001 paid 1000 for invoice inv-123 due on 2024-03-15"
```

### Rules

- Parse memo for "paying for:" or "paying off:" (case-insensitive)
- Extract invoice ID after the colon
- Find matching invoice in the list
- Return "could not be matched" if ID not found

---

## Step 2: Match by Amount

### Description

If no invoice ID in memo, find an invoice with the exact same amount.
If multiple invoices have the same amount, choose the one with the **earliest due date**.

### Sample Input/Output

```python
payment = "payment-002, 500, Monthly subscription"
invoices = [
    "inv-001, 2024-03-22, 1000",
    "inv-002, 2024-02-05, 500",
    "inv-003, 2024-03-01, 500",
    "inv-004, 2024-01-15, 500"
]

# Returns: "Payment payment-002 paid 500 for invoice inv-004 due on 2024-01-15"
# inv-004 has the earliest date among invoices with amount 500
```

### Rules

- Try ID match first (Step 1)
- If no ID match, find invoices with matching amount
- Select invoice with earliest due date
- Dates can be compared as strings (YYYY-MM-DD format)

---

## Step 3: Fuzzy Match (Forgiveness)

### Description

Add a "forgiveness" threshold to handle bank fees or rounding differences.
If exact amount match fails, find invoices within the tolerance range.

**Priority order:**
1. ID match (highest priority)
2. Exact amount match
3. Fuzzy amount match (lowest priority)

### Function Signature

```python
def reconcile_payment(payment: str, invoices: List[str], forgiveness: int = 0) -> str:
```

### Sample Input/Output

**Example 1: Exact match wins over fuzzy**
```python
payment = "payment-003, 98, Customer payment"
invoices = [
    "inv-100, 2024-03-15, 100",
    "inv-200, 2024-02-20, 98",
    "inv-300, 2024-01-10, 102"
]
forgiveness = 5

# Returns: "Payment payment-003 paid 98 for invoice inv-200 due on 2024-02-20"
# inv-200 matches exactly (98 == 98)
```

**Example 2: Fuzzy match with earliest date**
```python
payment = "payment-004, 95, Customer payment"
invoices = [
    "inv-100, 2024-03-15, 100",
    "inv-300, 2024-01-10, 97"
]
forgiveness = 5

# Returns: "Payment payment-004 paid 95 for invoice inv-300 due on 2024-01-10"
# Both within range [90, 100], inv-300 is earlier
```

### Rules

- Fuzzy range: `[payment_amount - forgiveness, payment_amount + forgiveness]`
- Exact matches always beat fuzzy matches
- Within same tier, earliest date wins
- Only use fuzzy matching if `forgiveness > 0`

---

## Constraints

- Payment and invoice IDs are alphanumeric with hyphens
- Amounts are positive integers (cents)
- Dates are valid YYYY-MM-DD format
- 1 ≤ number of invoices ≤ 10,000
- 0 ≤ forgiveness ≤ 1000

---

## Notes

- Each step builds on previous steps
- Always check ID match first, regardless of amounts
- The priority order is critical: ID > Exact Amount > Fuzzy Amount
- Test edge cases: exact forgiveness boundary, multiple same-amount invoices
