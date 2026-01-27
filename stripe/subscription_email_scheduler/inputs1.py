# Part 1: Scheduling Basics
# Send emails based on subscription timeline

part = 1

# Test case 1: Basic two users
user_accounts_1 = [
    {"name": "John", "plan": "Silver", "account_date": 0, "duration": 30},
    {"name": "Alice", "plan": "Gold", "account_date": 1, "duration": 15}
]

send_schedule_1 = {
    "start": "Welcome",
    -15: "Upcoming expiration",
    "end": "Expired"
}

expected_1 = """0: [Welcome] Subscription for John (Silver)
1: [Welcome] Subscription for Alice (Gold)
1: [Upcoming expiration] Subscription for Alice (Gold)
15: [Upcoming expiration] Subscription for John (Silver)
16: [Expired] Subscription for Alice (Gold)
30: [Expired] Subscription for John (Silver)"""

# Test case 2: Single user, simple schedule
user_accounts_2 = [
    {"name": "Bob", "plan": "Basic", "account_date": 5, "duration": 10}
]

send_schedule_2 = {
    "start": "Welcome",
    "end": "Expired"
}

# Bob: starts day 5, ends day 15
expected_2 = """5: [Welcome] Subscription for Bob (Basic)
15: [Expired] Subscription for Bob (Basic)"""

# Test case 3: Multiple offset keys
user_accounts_3 = [
    {"name": "Carol", "plan": "Premium", "account_date": 0, "duration": 30}
]

send_schedule_3 = {
    "start": "Welcome",
    -7: "One week warning",
    -3: "Three day warning",
    -1: "Last day warning",
    "end": "Expired"
}

# Carol: ends day 30
# Warnings: day 23 (-7), day 27 (-3), day 29 (-1)
expected_3 = """0: [Welcome] Subscription for Carol (Premium)
23: [One week warning] Subscription for Carol (Premium)
27: [Three day warning] Subscription for Carol (Premium)
29: [Last day warning] Subscription for Carol (Premium)
30: [Expired] Subscription for Carol (Premium)"""

# Test case 4: Users starting on same day
user_accounts_4 = [
    {"name": "Dan", "plan": "Gold", "account_date": 0, "duration": 20},
    {"name": "Eve", "plan": "Silver", "account_date": 0, "duration": 25}
]

send_schedule_4 = {
    "start": "Welcome",
    -10: "Reminder",
    "end": "Expired"
}

# Dan: ends 20, reminder day 10
# Eve: ends 25, reminder day 15
expected_4 = """0: [Welcome] Subscription for Dan (Gold)
0: [Welcome] Subscription for Eve (Silver)
10: [Reminder] Subscription for Dan (Gold)
15: [Reminder] Subscription for Eve (Silver)
20: [Expired] Subscription for Dan (Gold)
25: [Expired] Subscription for Eve (Silver)"""

test_cases = [
    {
        "user_accounts": user_accounts_1,
        "send_schedule": send_schedule_1,
        "expected": expected_1
    },
    {
        "user_accounts": user_accounts_2,
        "send_schedule": send_schedule_2,
        "expected": expected_2
    },
    {
        "user_accounts": user_accounts_3,
        "send_schedule": send_schedule_3,
        "expected": expected_3
    },
    {
        "user_accounts": user_accounts_4,
        "send_schedule": send_schedule_4,
        "expected": expected_4
    },
]
