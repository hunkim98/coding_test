Account Balance Manager

Challenge Summary

You need to build a system to manage bank accounts. This system will track money moving between accounts. It must also follow specific rules about keeping balances positive and handling empty accounts.

The challenge has three steps:

1. Calculating Totals: Add up transactions to find the final money count.
2. Stopping Overdrafts: Stop a transaction if an account runs out of money.
3. Covering Shortfalls: Use a main bank account to pay if a user does not have enough money.

Input Format

You get a list of transactions. Each item has:

- account_id: The ID name of the account.
- amount: The money involved. Positive numbers are deposits. Negative numbers are withdrawals.

```python
transactions = [
    {"account_id": "account_A", "amount": 100},
    {"account_id": "account_B", "amount": 50},
    {"account_id": "account_A", "amount": -30},
    {"account_id": "account_B", "amount": -80}
]
```

Step 1: Calculating Totals

Goal

Write a function called `get_account_balances(transactions)`. It should go through all transactions and calculate the final total for each account. Only return accounts that have money left (positive balance).

Example

Input:

```python
transactions = [
    {"account_id": "account_A", "amount": 100},
    {"account_id": "account_B", "amount": 50},
    {"account_id": "account_A", "amount": -30},
    {"account_id": "account_C", "amount": 200},
    {"account_id": "account_B", "amount": -50}
]
```

Output:

```python
get_account_balances(transactions)
# Returns: {"account_A": 70, "account_C": 200}
#
# Math:
# account_A: 100 - 30 = 70 (Positive, keep it)
# account_B: 50 - 50 = 0 (Zero, remove it)
# account_C: 200 (Positive, keep it)
```

Requirements

- Process the list in order.
- Group the money totals by account ID.
- Only return accounts with a balance greater than 0.
- Return a dictionary.

What to watch out for:

- An empty list of transactions.
- All accounts having zero balance.

Step 2: Stopping Overdrafts

Goal

Update your code to check the balance before making a change. If a withdrawal makes the balance negative, reject it. Return two things: the final balances and a list of the rejected transactions.

Function name: `process_transactions(transactions)`.

Example

Input:

```python
transactions = [
    {"account_id": "account_A", "amount": 100},
    {"account_id": "account_A", "amount": -150},  # Result is -50
    {"account_id": "account_B", "amount": 50},
    {"account_id": "account_A", "amount": -80},   # Valid: 100 - 80 = 20
    {"account_id": "account_B", "amount": -100}   # Result is -50
]
```

Output:

```python
process_transactions(transactions)
# Returns: (
#     {"account_A": 20, "account_B": 50},
#     [
#         {"account_id": "account_A", "amount": -150},
#         {"account_id": "account_B", "amount": -100}
#     ]
# )
#
# Steps:
# 1. account_A +100 → balance: 100 (OK)
# 2. account_A -150 → makes balance -50 (REJECT)
# 3. account_B +50 → balance: 50 (OK)
# 4. account_A -80 → balance: 20 (OK)
# 5. account_B -100 → makes balance -50 (REJECT)
```

Requirements

- Check items in order.
- Do not allow a transaction if the result is negative.
- Deposits (adding money) are always allowed.
- Keep a list of rejected items in the correct order.
- Include accounts with zero balance in the final list.

Key Notes:

- Adding money is always safe.
- You must check the math before changing the dictionary.
- The order of the rejected list matters.

Step 3: Covering Negative Balances

Goal

Now, the bank will help users. If a transaction makes the balance negative, do not reject it. Instead, take money from a special "platform account" to fill the gap. The user's account should end up at exactly zero.

Write `process_with_coverage(transactions, platform_account_id)`. Return the total amount of money the platform account had to pay.

Example

Input:

```python
transactions = [
    {"account_id": "platform", "amount": 1000},
    {"account_id": "account_A", "amount": 100},
    {"account_id": "account_A", "amount": -150},  # Needs 50 from bank
    {"account_id": "account_B", "amount": 50},
    {"account_id": "account_B", "amount": -100},  # Needs 50 from bank
    {"account_id": "account_A", "amount": -30}    # Needs 30 from bank
]

platform_account_id = "platform"
```

Output:

```python
process_with_coverage(transactions, "platform")
# Returns: 130
#
# Steps:
# 1. platform +1000 → platform has 1000
# 2. account_A +100 → account_A has 100
# 3. account_A -150 → result -50. Bank pays 50.
#    account_A is now 0. Platform is 950. Total paid: 50.
# 4. account_B +50 → account_B has 50
# 5. account_B -100 → result -50. Bank pays 50.
#    account_B is now 0. Platform is 900. Total paid: 100.
# 6. account_A -30 → result -30. Bank pays 30.
#    account_A is now 0. Platform is 870. Total paid: 130.
```

Requirements

- The function takes an extra input for the platform account ID.
- If a balance goes negative, transfer enough money to make it zero.
- The transaction still happens (the user balance becomes 0).
- Return the total money paid by the platform.
- Assume the platform account has enough money.

Key Notes:

- The platform account behaves like a normal account for its own transactions.
- Only cover regular users, not the platform itself.
- If the balance would be -50, you need 50 coverage.
- Ask the interviewer: Should we track the platform account balance? (This code does).
