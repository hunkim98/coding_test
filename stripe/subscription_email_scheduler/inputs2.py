# Part 2: Changing Plans
# Handle users switching subscription plans

part = 2

# Test case 1: One user changes plan
user_accounts_1 = [
    {"name": "John", "plan": "Silver", "account_date": 0, "duration": 30},
    {"name": "Alice", "plan": "Gold", "account_date": 1, "duration": 15}
]

send_schedule_1 = {
    "start": "Welcome",
    -15: "Upcoming expiration",
    "end": "Expired"
}

plan_changes_1 = [
    {"name": "John", "new_plan": "Gold", "change_date": 5}
]

expected_1 = """0: [Welcome] Subscription for John (Silver)
1: [Welcome] Subscription for Alice (Gold)
1: [Upcoming expiration] Subscription for Alice (Gold)
5: [Changed] Subscription for John (Gold)
15: [Upcoming expiration] Subscription for John (Gold)
16: [Expired] Subscription for Alice (Gold)
30: [Expired] Subscription for John (Gold)"""

# Test case 2: Multiple plan changes for same user
user_accounts_2 = [
    {"name": "Bob", "plan": "Basic", "account_date": 0, "duration": 30}
]

send_schedule_2 = {
    "start": "Welcome",
    -10: "Reminder",
    "end": "Expired"
}

plan_changes_2 = [
    {"name": "Bob", "new_plan": "Silver", "change_date": 5},
    {"name": "Bob", "new_plan": "Gold", "change_date": 15}
]

# Bob: Welcome at Basic, changes to Silver day 5, Gold day 15
# Reminder day 20, Expired day 30 should show Gold
expected_2 = """0: [Welcome] Subscription for Bob (Basic)
5: [Changed] Subscription for Bob (Silver)
15: [Changed] Subscription for Bob (Gold)
20: [Reminder] Subscription for Bob (Gold)
30: [Expired] Subscription for Bob (Gold)"""

# Test case 3: Multiple users with changes
user_accounts_3 = [
    {"name": "Carol", "plan": "Basic", "account_date": 0, "duration": 20},
    {"name": "Dan", "plan": "Basic", "account_date": 0, "duration": 25}
]

send_schedule_3 = {
    "start": "Welcome",
    "end": "Expired"
}

plan_changes_3 = [
    {"name": "Carol", "new_plan": "Gold", "change_date": 10},
    {"name": "Dan", "new_plan": "Silver", "change_date": 5}
]

expected_3 = """0: [Welcome] Subscription for Carol (Basic)
0: [Welcome] Subscription for Dan (Basic)
5: [Changed] Subscription for Dan (Silver)
10: [Changed] Subscription for Carol (Gold)
20: [Expired] Subscription for Carol (Gold)
25: [Expired] Subscription for Dan (Silver)"""

# Test case 4: Plan change same day as notification
user_accounts_4 = [
    {"name": "Eve", "plan": "Silver", "account_date": 0, "duration": 20}
]

send_schedule_4 = {
    "start": "Welcome",
    -10: "Reminder",
    "end": "Expired"
}

plan_changes_4 = [
    {"name": "Eve", "new_plan": "Gold", "change_date": 10}  # Same day as reminder
]

# Plan change should be processed before notification on same day
expected_4 = """0: [Welcome] Subscription for Eve (Silver)
10: [Changed] Subscription for Eve (Gold)
10: [Reminder] Subscription for Eve (Gold)
20: [Expired] Subscription for Eve (Gold)"""

test_cases = [
    {
        "user_accounts": user_accounts_1,
        "send_schedule": send_schedule_1,
        "changes": plan_changes_1,
        "expected": expected_1
    },
    {
        "user_accounts": user_accounts_2,
        "send_schedule": send_schedule_2,
        "changes": plan_changes_2,
        "expected": expected_2
    },
    {
        "user_accounts": user_accounts_3,
        "send_schedule": send_schedule_3,
        "changes": plan_changes_3,
        "expected": expected_3
    },
    {
        "user_accounts": user_accounts_4,
        "send_schedule": send_schedule_4,
        "changes": plan_changes_4,
        "expected": expected_4
    },
]
