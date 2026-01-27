# Step 3: Client History (Affinity)
# Prioritize workers who helped the same client before

part = 3

# Test case 1: Basic affinity
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

expected_1 = [
    {"taskId": "task1", "worker": "alice"},
    {"taskId": "task2", "worker": "bob"},
    {"taskId": "task3", "worker": "alice"},
    {"taskId": "task4", "worker": "alice"},
    {"taskId": "task5", "worker": "bob"}
]

# Test case 2: Affinity beats lower workload
workers_2 = [
    {"name": "alice", "specialty": "support"},
    {"name": "bob", "specialty": "support"}
]

tasks_2 = [
    {"id": "t1", "duration": 10, "requiredSpecialties": ["support"], "accountId": "client_a"},
    {"id": "t2", "duration": 5, "requiredSpecialties": ["support"], "accountId": "client_a"}
]

# alice gets client_a, even though she's busier after t1
# t1: alice(0) gets it
# t2: alice has affinity for client_a, bob(0) is less busy but no affinity
expected_2 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "alice"}
]

# Test case 3: Multiple workers with same affinity
workers_3 = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "billing"},
    {"name": "charlie", "specialty": "billing"}
]

tasks_3 = [
    {"id": "t1", "duration": 5, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "t2", "duration": 3, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "t3", "duration": 7, "requiredSpecialties": ["billing"], "accountId": "acme"}
]

# All tasks go to alice (first to establish affinity)
expected_3 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "alice"},
    {"taskId": "t3", "worker": "alice"}
]

# Test case 4: Different accounts, different workers
workers_4 = [
    {"name": "alice", "specialty": "support"},
    {"name": "bob", "specialty": "support"},
    {"name": "charlie", "specialty": "support"}
]

tasks_4 = [
    {"id": "t1", "duration": 5, "requiredSpecialties": ["support"], "accountId": "A"},
    {"id": "t2", "duration": 5, "requiredSpecialties": ["support"], "accountId": "B"},
    {"id": "t3", "duration": 5, "requiredSpecialties": ["support"], "accountId": "C"},
    {"id": "t4", "duration": 2, "requiredSpecialties": ["support"], "accountId": "A"},
    {"id": "t5", "duration": 2, "requiredSpecialties": ["support"], "accountId": "B"},
    {"id": "t6", "duration": 2, "requiredSpecialties": ["support"], "accountId": "C"}
]

# Each worker gets their own account
expected_4 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "bob"},
    {"taskId": "t3", "worker": "charlie"},
    {"taskId": "t4", "worker": "alice"},
    {"taskId": "t5", "worker": "bob"},
    {"taskId": "t6", "worker": "charlie"}
]

# Test case 5: No affinity falls back to workload
workers_5 = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "billing"}
]

tasks_5 = [
    {"id": "t1", "duration": 10, "requiredSpecialties": ["billing"], "accountId": "X"},
    {"id": "t2", "duration": 5, "requiredSpecialties": ["billing"], "accountId": "Y"},
    {"id": "t3", "duration": 3, "requiredSpecialties": ["billing"], "accountId": "Z"}
]

# No shared accounts, pure workload balancing
# t1: alice(0), bob(0) -> alice
# t2: alice(10), bob(0) -> bob
# t3: alice(10), bob(5) -> bob
expected_5 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "bob"},
    {"taskId": "t3", "worker": "bob"}
]

test_cases = [
    {"workers": workers_1, "tasks": tasks_1, "expected": expected_1},
    {"workers": workers_2, "tasks": tasks_2, "expected": expected_2},
    {"workers": workers_3, "tasks": tasks_3, "expected": expected_3},
    {"workers": workers_4, "tasks": tasks_4, "expected": expected_4},
    {"workers": workers_5, "tasks": tasks_5, "expected": expected_5},
]
