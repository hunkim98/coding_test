# Part 3: Edge Cases
# Handle burst traffic, out-of-order timestamps, time gaps

part = 3

# Test case 1: Burst traffic (multiple hits at same timestamp)
config_1 = {"max_requests": 3, "window_seconds": 10}
operations_1 = [
    ("hit", "user_1", 5),
    ("hit", "user_1", 5),       # Same timestamp
    ("allowed", "user_1", 5),  # 2 hits, True
    ("hit", "user_1", 5),       # Third hit same time
    ("allowed", "user_1", 5),  # 3 hits = limit, False
    ("hit", "user_1", 5),       # Fourth hit (over limit)
    ("allowed", "user_1", 5),  # 4 hits > limit, False
]
expected_1 = [True, False, False]

# Test case 2: Out-of-order timestamps
config_2 = {"max_requests": 3, "window_seconds": 10}
operations_2 = [
    ("hit", "user_2", 10),
    ("hit", "user_2", 8),      # Older timestamp arrives late
    ("hit", "user_2", 12),
    ("allowed", "user_2", 12), # All 3 in window, False
    ("hit", "user_2", 5),      # Even older timestamp
    ("allowed", "user_2", 12), # t=5 still in window (12-10=2, 5>2), 4 hits
]
expected_2 = [False, False]

# Test case 3: Large time gap
config_3 = {"max_requests": 2, "window_seconds": 10}
operations_3 = [
    ("hit", "user_3", 1),
    ("hit", "user_3", 2),
    ("allowed", "user_3", 3),     # 2 hits, False
    ("allowed", "user_3", 1000),  # Huge gap, all old, True
    ("hit", "user_3", 1000),
    ("allowed", "user_3", 1000),  # 1 hit, True
]
expected_3 = [False, True, True]

# Test case 4: Mixed scenarios
config_4 = {"max_requests": 4, "window_seconds": 5}
operations_4 = [
    ("hit", "user", 1),
    ("hit", "user", 1),        # Burst
    ("hit", "user", 3),
    ("allowed", "user", 3),    # 3 hits, True
    ("hit", "user", 2),        # Out of order
    ("allowed", "user", 3),    # 4 hits, False
    ("allowed", "user", 10),   # All outside window, True
]
expected_4 = [True, False, True]

# Test case 5: Out-of-order with window boundary
config_5 = {"max_requests": 3, "window_seconds": 10}
operations_5 = [
    ("hit", "user", 15),
    ("hit", "user", 20),
    ("hit", "user", 12),       # Out of order, but still in window at t=20
    ("allowed", "user", 20),   # 3 hits (12,15,20 all in [10,20]), False
    ("hit", "user", 5),        # Very old, outside window at t=20
    ("allowed", "user", 20),   # t=5 is outside [10,20], still 3 hits
]
expected_5 = [False, False]

test_cases = [
    {"config": config_1, "operations": operations_1, "expected": expected_1},
    {"config": config_2, "operations": operations_2, "expected": expected_2},
    {"config": config_3, "operations": operations_3, "expected": expected_3},
    {"config": config_4, "operations": operations_4, "expected": expected_4},
    {"config": config_5, "operations": operations_5, "expected": expected_5},
]
