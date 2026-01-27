# Step 4: Handling Offline Workers
# Workers can go offline after specific tasks

part = 4

# Test case 1: Basic offline handling
workers_1 = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "billing"},
    {"name": "charlie", "specialty": "billing"}
]

tasks_1 = [
    {"id": "task1", "duration": 5, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "task2", "duration": 3, "requiredSpecialties": ["billing"], "accountId": "globex"},
    {"id": "task3", "duration": 7, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "task4", "duration": 2, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "task5", "duration": 4, "requiredSpecialties": ["billing"], "accountId": "globex"}
]

offlineEvents_1 = [
    {"worker": "alice", "afterTaskIndex": 2}
]

# alice offline after task index 2 (task3)
expected_1 = [
    {"taskId": "task1", "worker": "alice"},
    {"taskId": "task2", "worker": "bob"},
    {"taskId": "task3", "worker": "alice"},
    {"taskId": "task4", "worker": "charlie"},  # alice offline, charlie gets acme
    {"taskId": "task5", "worker": "bob"}
]

# Test case 2: Multiple workers go offline
workers_2 = [
    {"name": "alice", "specialty": "support"},
    {"name": "bob", "specialty": "support"},
    {"name": "charlie", "specialty": "support"}
]

tasks_2 = [
    {"id": "t1", "duration": 5, "requiredSpecialties": ["support"], "accountId": "X"},
    {"id": "t2", "duration": 3, "requiredSpecialties": ["support"], "accountId": "Y"},
    {"id": "t3", "duration": 7, "requiredSpecialties": ["support"], "accountId": "Z"},
    {"id": "t4", "duration": 2, "requiredSpecialties": ["support"], "accountId": "X"},
    {"id": "t5", "duration": 4, "requiredSpecialties": ["support"], "accountId": "Y"}
]

offlineEvents_2 = [
    {"worker": "alice", "afterTaskIndex": 0},
    {"worker": "bob", "afterTaskIndex": 1}
]

# alice offline after t1, bob offline after t2
expected_2 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "bob"},
    {"taskId": "t3", "worker": "charlie"},
    {"taskId": "t4", "worker": "charlie"},
    {"taskId": "t5", "worker": "charlie"}
]

# Test case 3: Worker goes offline immediately
workers_3 = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "billing"}
]

tasks_3 = [
    {"id": "t1", "duration": 5, "requiredSpecialties": ["billing"], "accountId": "A"},
    {"id": "t2", "duration": 3, "requiredSpecialties": ["billing"], "accountId": "A"},
    {"id": "t3", "duration": 7, "requiredSpecialties": ["billing"], "accountId": "A"}
]

offlineEvents_3 = [
    {"worker": "alice", "afterTaskIndex": 0}
]

# alice gets t1, then goes offline
# bob takes over account A even without history
expected_3 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "bob"},
    {"taskId": "t3", "worker": "bob"}
]

# Test case 4: Affinity worker goes offline
workers_4 = [
    {"name": "alice", "specialty": "support"},
    {"name": "bob", "specialty": "support"},
    {"name": "charlie", "specialty": "support"}
]

tasks_4 = [
    {"id": "t1", "duration": 5, "requiredSpecialties": ["support"], "accountId": "acme"},
    {"id": "t2", "duration": 3, "requiredSpecialties": ["support"], "accountId": "globex"},
    {"id": "t3", "duration": 2, "requiredSpecialties": ["support"], "accountId": "acme"},
    {"id": "t4", "duration": 4, "requiredSpecialties": ["support"], "accountId": "acme"}
]

offlineEvents_4 = [
    {"worker": "alice", "afterTaskIndex": 2}
]

# alice handles acme (t1, t3), bob handles globex (t2)
# alice goes offline after t3
# t4 (acme) goes to charlie (no affinity available)
expected_4 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "bob"},
    {"taskId": "t3", "worker": "alice"},
    {"taskId": "t4", "worker": "charlie"}
]

# Test case 5: No offline events
workers_5 = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "billing"}
]

tasks_5 = [
    {"id": "t1", "duration": 5, "requiredSpecialties": ["billing"], "accountId": "X"},
    {"id": "t2", "duration": 3, "requiredSpecialties": ["billing"], "accountId": "X"}
]

offlineEvents_5 = []

# Normal affinity behavior
expected_5 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "alice"}
]

test_cases = [
    {"workers": workers_1, "tasks": tasks_1, "offlineEvents": offlineEvents_1, "expected": expected_1},
    {"workers": workers_2, "tasks": tasks_2, "offlineEvents": offlineEvents_2, "expected": expected_2},
    {"workers": workers_3, "tasks": tasks_3, "offlineEvents": offlineEvents_3, "expected": expected_3},
    {"workers": workers_4, "tasks": tasks_4, "offlineEvents": offlineEvents_4, "expected": expected_4},
    {"workers": workers_5, "tasks": tasks_5, "offlineEvents": offlineEvents_5, "expected": expected_5},
]
