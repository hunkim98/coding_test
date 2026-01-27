# Step 2: Matching Skills
# Only assign to workers with required specialty

part = 2

# Test case 1: Basic skill matching
workers_1 = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "technical"},
    {"name": "charlie", "specialty": "billing"},
    {"name": "diana", "specialty": "technical"}
]

tasks_1 = [
    {"id": "task1", "duration": 5, "requiredSpecialties": ["billing"]},
    {"id": "task2", "duration": 3, "requiredSpecialties": ["technical"]},
    {"id": "task3", "duration": 7, "requiredSpecialties": ["billing", "technical"]},
    {"id": "task4", "duration": 2, "requiredSpecialties": ["billing"]},
    {"id": "task5", "duration": 4, "requiredSpecialties": ["technical"]}
]

expected_1 = [
    {"taskId": "task1", "worker": "alice"},
    {"taskId": "task2", "worker": "bob"},
    {"taskId": "task3", "worker": "charlie"},
    {"taskId": "task4", "worker": "alice"},
    {"taskId": "task5", "worker": "diana"}
]

# Test case 2: Single specialty
workers_2 = [
    {"name": "alice", "specialty": "support"},
    {"name": "bob", "specialty": "support"},
    {"name": "charlie", "specialty": "support"}
]

tasks_2 = [
    {"id": "t1", "duration": 5, "requiredSpecialties": ["support"]},
    {"id": "t2", "duration": 3, "requiredSpecialties": ["support"]},
    {"id": "t3", "duration": 7, "requiredSpecialties": ["support"]}
]

# All support, load balancing takes over
expected_2 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "bob"},
    {"taskId": "t3", "worker": "charlie"}
]

# Test case 3: No matching skill (task skipped)
workers_3 = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "billing"}
]

tasks_3 = [
    {"id": "t1", "duration": 5, "requiredSpecialties": ["billing"]},
    {"id": "t2", "duration": 3, "requiredSpecialties": ["technical"]},  # No one has this
    {"id": "t3", "duration": 7, "requiredSpecialties": ["billing"]}
]

# t2 is skipped (no technical workers)
expected_3 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t3", "worker": "bob"}
]

# Test case 4: Multiple specialties accepted
workers_4 = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "technical"},
    {"name": "charlie", "specialty": "sales"}
]

tasks_4 = [
    {"id": "t1", "duration": 5, "requiredSpecialties": ["billing", "technical", "sales"]},
    {"id": "t2", "duration": 3, "requiredSpecialties": ["billing", "technical", "sales"]},
    {"id": "t3", "duration": 7, "requiredSpecialties": ["billing", "technical", "sales"]}
]

# All workers eligible for all tasks
expected_4 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "bob"},
    {"taskId": "t3", "worker": "charlie"}
]

# Test case 5: Workload tie-breaker with skills
workers_5 = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "billing"},
    {"name": "charlie", "specialty": "technical"}
]

tasks_5 = [
    {"id": "t1", "duration": 5, "requiredSpecialties": ["billing"]},
    {"id": "t2", "duration": 5, "requiredSpecialties": ["billing"]},
    {"id": "t3", "duration": 3, "requiredSpecialties": ["billing"]}
]

# t1: alice(0), bob(0) -> alice
# t2: alice(5), bob(0) -> bob
# t3: alice(5), bob(5) -> alice (tie, alice first)
expected_5 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "bob"},
    {"taskId": "t3", "worker": "alice"}
]

test_cases = [
    {"workers": workers_1, "tasks": tasks_1, "expected": expected_1},
    {"workers": workers_2, "tasks": tasks_2, "expected": expected_2},
    {"workers": workers_3, "tasks": tasks_3, "expected": expected_3},
    {"workers": workers_4, "tasks": tasks_4, "expected": expected_4},
    {"workers": workers_5, "tasks": tasks_5, "expected": expected_5},
]
