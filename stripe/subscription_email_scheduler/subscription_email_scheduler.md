# Subscription Email Scheduler

## Problem Description

Build an automated email system for a subscription service. The system sends emails to users at specific times based on their subscription lifecycle.

---

## Data Format

### User Accounts

```python
[
    {
        "name": "John",
        "plan": "Silver",
        "account_date": 0,   # Day subscription started
        "duration": 30       # Length in days
    }
]
```

### Send Schedule

```python
{
    "start": "Welcome",        # Send on subscription start day
    -15: "Upcoming expiration", # 15 days before end
    "end": "Expired"           # Send on expiration day
}
```

---

## Part 1: Scheduling Basics

### Task

Write a function `send_emails(user_accounts, send_schedule)` to generate email events.

### Schedule Keys

- `"start"`: Send on the day the subscription begins (account_date)
- `"end"`: Send on the day the subscription expires (account_date + duration)
- **Number keys** (e.g., -15): Days relative to end date

### Example

**Input:**
```python
user_accounts = [
    {"name": "John", "plan": "Silver", "account_date": 0, "duration": 30},
    {"name": "Alice", "plan": "Gold", "account_date": 1, "duration": 15}
]

send_schedule = {
    "start": "Welcome",
    -15: "Upcoming expiration",
    "end": "Expired"
}
```

**Output:**
```
0: [Welcome] Subscription for John (Silver)
1: [Welcome] Subscription for Alice (Gold)
1: [Upcoming expiration] Subscription for Alice (Gold)
15: [Upcoming expiration] Subscription for John (Silver)
16: [Expired] Subscription for Alice (Gold)
30: [Expired] Subscription for John (Silver)
```

### Output Format

- Format: `{day}: [{message_type}] Subscription for {name} ({plan})`
- Group by day (ascending order)
- Multiple emails on same day appear on separate lines

### Key Logic

- End date = account_date + duration
- For number key X: notification_date = end_date + X
- Handle any number key generically (don't hardcode -15)

---

## Part 2: Changing Plans

### Task

Update the system to handle plan changes. Users can switch plans mid-subscription.

### Additional Input

```python
plan_changes = [
    {"name": "John", "new_plan": "Gold", "change_date": 5}
]
```

### Rules

- Send a "Changed" email on the change date
- Update the plan name for all future emails
- End date remains unchanged

### Example

**Input:**
```python
user_accounts = [
    {"name": "John", "plan": "Silver", "account_date": 0, "duration": 30},
    {"name": "Alice", "plan": "Gold", "account_date": 1, "duration": 15}
]

plan_changes = [
    {"name": "John", "new_plan": "Gold", "change_date": 5}
]
```

**Output:**
```
0: [Welcome] Subscription for John (Silver)
1: [Welcome] Subscription for Alice (Gold)
1: [Upcoming expiration] Subscription for Alice (Gold)
5: [Changed] Subscription for John (Gold)
15: [Upcoming expiration] Subscription for John (Gold)
16: [Expired] Subscription for Alice (Gold)
30: [Expired] Subscription for John (Gold)
```

Note: John's plan shows "Gold" for day 15 and 30 emails.

---

## Part 3: Handling Renewals

### Task

Add support for renewals. Users can extend their subscription duration.

### Additional Input

Changes can now include renewals:

```python
changes = [
    {"name": "John", "new_plan": "Gold", "change_date": 5},      # Plan change
    {"name": "Alice", "extension": 15, "change_date": 3}         # Renewal
]
```

### Rules

- Send a "Renewed" email on renewal date
- Add extension to the current end date
- **Recalculate** all future emails based on new end date

### Example

**Input:**
```python
user_accounts = [
    {"name": "John", "plan": "Silver", "account_date": 0, "duration": 30},
    {"name": "Alice", "plan": "Gold", "account_date": 1, "duration": 15}
]

changes = [
    {"name": "John", "new_plan": "Gold", "change_date": 5},
    {"name": "Alice", "extension": 15, "change_date": 3}
]
```

**Output:**
```
0: [Welcome] Subscription for John (Silver)
1: [Welcome] Subscription for Alice (Gold)
1: [Upcoming expiration] Subscription for Alice (Gold)
3: [Renewed] Subscription for Alice (Gold)
5: [Changed] Subscription for John (Gold)
15: [Upcoming expiration] Subscription for John (Gold)
16: [Upcoming expiration] Subscription for Alice (Gold)
30: [Expired] Subscription for John (Gold)
31: [Expired] Subscription for Alice (Gold)
```

### Alice's Timeline Explained

1. **Original**: Ends day 16, upcoming expiration on day 1
2. **Day 3 renewal**: New end = 16 + 15 = 31
3. **After renewal**: New upcoming expiration on day 16 (31 - 15)
4. Alice gets "Upcoming expiration" twice (day 1 for original, day 16 for extended)

---

## Event Priority

When multiple events occur on the same day, process in this order:
1. Plan changes
2. Renewals
3. Notifications

---

## Constraints

- Days are non-negative integers
- Names are unique strings
- Schedule keys are either "start", "end", or negative integers
- Changes happen during active subscription period
- Extension days are positive integers

---

## Test Format

```python
def send_emails(user_accounts, send_schedule, changes=None) -> str:
    """
    Returns multiline string of email events in chronological order.
    """
    pass
```
