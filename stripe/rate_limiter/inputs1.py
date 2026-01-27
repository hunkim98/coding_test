# Part 1: Basic Rate Limiter
# Implement sliding window rate limiting

part = 1

# Test case 1: Basic usage
config_1 = {"max_requests": 3, "window_seconds": 10}
operations_1 = [
    ("hit", "user_1", 1),
    ("hit", "user_1", 2),
    ("allowed", "user_1", 3),   # 2 hits < 3, should be True
    ("hit", "user_1", 3),
    ("allowed", "user_1", 4),   # 3 hits = limit, should be False
    ("allowed", "user_1", 12),  # t=1,2 outside window, only t=3 remains
]
expected_1 = [True, False, True]

# Test case 2: Multiple users
config_2 = {"max_requests": 2, "window_seconds": 5}
operations_2 = [
    ("hit", "alice", 1),
    ("hit", "bob", 1),
    ("allowed", "alice", 2),  # alice: 1 hit, True
    ("allowed", "bob", 2),    # bob: 1 hit, True
    ("hit", "alice", 2),
    ("allowed", "alice", 3),  # alice: 2 hits = limit, False
    ("allowed", "bob", 3),    # bob: 1 hit, True
]
expected_2 = [True, True, False, True]

# Test case 3: New user
config_3 = {"max_requests": 5, "window_seconds": 60}
operations_3 = [
    ("allowed", "new_user", 100),  # No history, True
    ("hit", "new_user", 100),
    ("allowed", "new_user", 100),  # 1 hit, True
]
expected_3 = [True, True]

# Test case 4: Window expiration
config_4 = {"max_requests": 2, "window_seconds": 10}
operations_4 = [
    ("hit", "user", 1),
    ("hit", "user", 5),
    ("allowed", "user", 8),   # Both hits in window, False
    ("allowed", "user", 12),  # t=1 outside, only t=5 remains, True
    ("allowed", "user", 16),  # Both outside window, True
]
expected_4 = [False, True, True]

test_cases = [
    {"config": config_1, "operations": operations_1, "expected": expected_1},
    {"config": config_2, "operations": operations_2, "expected": expected_2},
    {"config": config_3, "operations": operations_3, "expected": expected_3},
    {"config": config_4, "operations": operations_4, "expected": expected_4},
]
