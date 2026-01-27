# Part 3: Handling Renewals
# Handle subscription extensions with recalculation

part = 3

# Test case 1: Plan change and renewal
user_accounts_1 = [
    {"name": "John", "plan": "Silver", "account_date": 0, "duration": 30},
    {"name": "Alice", "plan": "Gold", "account_date": 1, "duration": 15}
]

send_schedule_1 = {
    "start": "Welcome",
    -15: "Upcoming expiration",
    "end": "Expired"
}

changes_1 = [
    {"name": "John", "new_plan": "Gold", "change_date": 5},
    {"name": "Alice", "extension": 15, "change_date": 3}
]

# Alice: original end 16, new end 31, new reminder at 16 (31-15)
expected_1 = """0: [Welcome] Subscription for John (Silver)
1: [Welcome] Subscription for Alice (Gold)
1: [Upcoming expiration] Subscription for Alice (Gold)
3: [Renewed] Subscription for Alice (Gold)
5: [Changed] Subscription for John (Gold)
15: [Upcoming expiration] Subscription for John (Gold)
16: [Upcoming expiration] Subscription for Alice (Gold)
30: [Expired] Subscription for John (Gold)
31: [Expired] Subscription for Alice (Gold)"""

# Test case 2: Multiple renewals for same user
user_accounts_2 = [
    {"name": "Bob", "plan": "Basic", "account_date": 0, "duration": 10}
]

send_schedule_2 = {
    "start": "Welcome",
    -5: "Reminder",
    "end": "Expired"
}

changes_2 = [
    {"name": "Bob", "extension": 10, "change_date": 3},  # End: 10 -> 20
    {"name": "Bob", "extension": 5, "change_date": 12}   # End: 20 -> 25
]

# Bob: starts 0, original end 10, reminder at 5
# After first renewal: end 20, new reminder at 15
# After second renewal: end 25, new reminder at 20
expected_2 = """0: [Welcome] Subscription for Bob (Basic)
3: [Renewed] Subscription for Bob (Basic)
5: [Reminder] Subscription for Bob (Basic)
12: [Renewed] Subscription for Bob (Basic)
15: [Reminder] Subscription for Bob (Basic)
20: [Reminder] Subscription for Bob (Basic)
25: [Expired] Subscription for Bob (Basic)"""

# Test case 3: Plan change then renewal
user_accounts_3 = [
    {"name": "Carol", "plan": "Silver", "account_date": 0, "duration": 20}
]

send_schedule_3 = {
    "start": "Welcome",
    -10: "Reminder",
    "end": "Expired"
}

changes_3 = [
    {"name": "Carol", "new_plan": "Gold", "change_date": 5},
    {"name": "Carol", "extension": 10, "change_date": 8}
]

# Carol: ends 20, reminder 10, changes to Gold day 5
# After renewal day 8: ends 30, new reminder 20
expected_3 = """0: [Welcome] Subscription for Carol (Silver)
5: [Changed] Subscription for Carol (Gold)
8: [Renewed] Subscription for Carol (Gold)
10: [Reminder] Subscription for Carol (Gold)
20: [Reminder] Subscription for Carol (Gold)
30: [Expired] Subscription for Carol (Gold)"""

# Test case 4: Renewal cancels scheduled expiration
user_accounts_4 = [
    {"name": "Dan", "plan": "Premium", "account_date": 0, "duration": 15}
]

send_schedule_4 = {
    "start": "Welcome",
    "end": "Expired"
}

changes_4 = [
    {"name": "Dan", "extension": 20, "change_date": 10}  # End: 15 -> 35
]

# Dan: original would expire day 15, after renewal expires day 35
expected_4 = """0: [Welcome] Subscription for Dan (Premium)
10: [Renewed] Subscription for Dan (Premium)
35: [Expired] Subscription for Dan (Premium)"""

# Test case 5: Renewal same day as original reminder
user_accounts_5 = [
    {"name": "Eve", "plan": "Gold", "account_date": 0, "duration": 20}
]

send_schedule_5 = {
    "start": "Welcome",
    -10: "Reminder",
    "end": "Expired"
}

changes_5 = [
    {"name": "Eve", "extension": 15, "change_date": 10}  # Renewal on original reminder day
]

# Original reminder day 10, renewal same day
# New end 35, new reminder day 25
expected_5 = """0: [Welcome] Subscription for Eve (Gold)
10: [Reminder] Subscription for Eve (Gold)
10: [Renewed] Subscription for Eve (Gold)
25: [Reminder] Subscription for Eve (Gold)
35: [Expired] Subscription for Eve (Gold)"""

test_cases = [
    {
        "user_accounts": user_accounts_1,
        "send_schedule": send_schedule_1,
        "changes": changes_1,
        "expected": expected_1
    },
    {
        "user_accounts": user_accounts_2,
        "send_schedule": send_schedule_2,
        "changes": changes_2,
        "expected": expected_2
    },
    {
        "user_accounts": user_accounts_3,
        "send_schedule": send_schedule_3,
        "changes": changes_3,
        "expected": expected_3
    },
    {
        "user_accounts": user_accounts_4,
        "send_schedule": send_schedule_4,
        "changes": changes_4,
        "expected": expected_4
    },
    {
        "user_accounts": user_accounts_5,
        "send_schedule": send_schedule_5,
        "changes": changes_5,
        "expected": expected_5
    },
]
