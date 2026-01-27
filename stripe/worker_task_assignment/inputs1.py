# Step 1: Balancing Workload
# Assign tasks to least busy worker

part = 1

# Test case 1: Basic example
workers_1 = ["alice", "bob", "charlie"]
tasks_1 = [
    {"id": "task1", "duration": 5},
    {"id": "task2", "duration": 3},
    {"id": "task3", "duration": 7},
    {"id": "task4", "duration": 2},
    {"id": "task5", "duration": 4}
]

expected_1 = [
    {"taskId": "task1", "worker": "alice"},
    {"taskId": "task2", "worker": "bob"},
    {"taskId": "task3", "worker": "charlie"},
    {"taskId": "task4", "worker": "bob"},
    {"taskId": "task5", "worker": "alice"}
]

# Test case 2: Two workers
workers_2 = ["alice", "bob"]
tasks_2 = [
    {"id": "t1", "duration": 10},
    {"id": "t2", "duration": 10},
    {"id": "t3", "duration": 5},
    {"id": "t4", "duration": 5}
]

# alice: t1(10), t3(5) = 15
# bob: t2(10), t4(5) = 15
expected_2 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "bob"},
    {"taskId": "t3", "worker": "alice"},
    {"taskId": "t4", "worker": "bob"}
]

# Test case 3: Single worker
workers_3 = ["solo"]
tasks_3 = [
    {"id": "task1", "duration": 5},
    {"id": "task2", "duration": 3},
    {"id": "task3", "duration": 7}
]

expected_3 = [
    {"taskId": "task1", "worker": "solo"},
    {"taskId": "task2", "worker": "solo"},
    {"taskId": "task3", "worker": "solo"}
]

# Test case 4: Tie-breaker test
workers_4 = ["a", "b", "c", "d"]
tasks_4 = [
    {"id": "t1", "duration": 1},
    {"id": "t2", "duration": 1},
    {"id": "t3", "duration": 1},
    {"id": "t4", "duration": 1},
    {"id": "t5", "duration": 1}
]

# All tied at 0, go in order: a, b, c, d, then a again
expected_4 = [
    {"taskId": "t1", "worker": "a"},
    {"taskId": "t2", "worker": "b"},
    {"taskId": "t3", "worker": "c"},
    {"taskId": "t4", "worker": "d"},
    {"taskId": "t5", "worker": "a"}
]

# Test case 5: Zero duration tasks
workers_5 = ["alice", "bob"]
tasks_5 = [
    {"id": "t1", "duration": 0},
    {"id": "t2", "duration": 0},
    {"id": "t3", "duration": 5}
]

# Zero duration doesn't change workload
# t1->alice(0), t2->alice(still 0, tie goes to first), t3->alice(still 0)
expected_5 = [
    {"taskId": "t1", "worker": "alice"},
    {"taskId": "t2", "worker": "alice"},
    {"taskId": "t3", "worker": "alice"}
]

test_cases = [
    {"workers": workers_1, "tasks": tasks_1, "expected": expected_1},
    {"workers": workers_2, "tasks": tasks_2, "expected": expected_2},
    {"workers": workers_3, "tasks": tasks_3, "expected": expected_3},
    {"workers": workers_4, "tasks": tasks_4, "expected": expected_4},
    {"workers": workers_5, "tasks": tasks_5, "expected": expected_5},
]
