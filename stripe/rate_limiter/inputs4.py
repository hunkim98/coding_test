# Part 4: Thread Safety
# Handle concurrent access with atomic check-and-hit

part = 4

# Test case 1: Atomic check_and_hit basic usage
config_1 = {"max_requests": 3, "window_seconds": 10}
operations_1 = [
    ("check_and_hit", "user_1", 1),  # 0 < 3, allowed, hit recorded -> True
    ("check_and_hit", "user_1", 2),  # 1 < 3, allowed -> True
    ("check_and_hit", "user_1", 3),  # 2 < 3, allowed -> True
    ("check_and_hit", "user_1", 4),  # 3 = limit, not allowed -> False
    ("check_and_hit", "user_1", 5),  # 3 = limit, not allowed -> False
]
expected_1 = [True, True, True, False, False]

# Test case 2: Window expiration with check_and_hit
config_2 = {"max_requests": 2, "window_seconds": 10}
operations_2 = [
    ("check_and_hit", "user", 1),   # True, recorded
    ("check_and_hit", "user", 5),   # True, recorded (2 hits)
    ("check_and_hit", "user", 8),   # False (at limit)
    ("check_and_hit", "user", 15),  # t=1 expired, only t=5 in window, True
    ("check_and_hit", "user", 16),  # t=5,15 in window (2 hits), False
]
expected_2 = [True, True, False, True, False]

# Test case 3: Multiple users thread safety
config_3 = {"max_requests": 2, "window_seconds": 5}
operations_3 = [
    ("check_and_hit", "alice", 1),  # True
    ("check_and_hit", "bob", 1),    # True (different user)
    ("check_and_hit", "alice", 2),  # True (2nd for alice)
    ("check_and_hit", "bob", 2),    # True (2nd for bob)
    ("check_and_hit", "alice", 3),  # False (alice at limit)
    ("check_and_hit", "bob", 3),    # False (bob at limit)
]
expected_3 = [True, True, True, True, False, False]

# Test case 4: Simulated race condition scenario
# This tests the logic that would prevent race conditions
config_4 = {"max_requests": 1, "window_seconds": 10}
operations_4 = [
    ("check_and_hit", "user", 1),  # First request: True, hit recorded
    ("check_and_hit", "user", 1),  # Simultaneous: False (already at limit)
    ("check_and_hit", "user", 1),  # Another attempt: False
    ("check_and_hit", "user", 15), # Window expired: True
]
expected_4 = [True, False, False, True]

# Test case 5: Mixed operations (hit, allowed, check_and_hit)
config_5 = {"max_requests": 3, "window_seconds": 10}
operations_5 = [
    ("hit", "user", 1),
    ("allowed", "user", 2),        # 1 hit, True
    ("check_and_hit", "user", 3),  # 1 < 3, True (now 2 hits)
    ("allowed", "user", 4),        # 2 hits, True
    ("check_and_hit", "user", 5),  # 2 < 3, True (now 3 hits)
    ("allowed", "user", 6),        # 3 hits, False
    ("check_and_hit", "user", 7),  # 3 = limit, False
]
expected_5 = [True, True, True, True, False, False]

test_cases = [
    {"config": config_1, "operations": operations_1, "expected": expected_1},
    {"config": config_2, "operations": operations_2, "expected": expected_2},
    {"config": config_3, "operations": operations_3, "expected": expected_3},
    {"config": config_4, "operations": operations_4, "expected": expected_4},
    {"config": config_5, "operations": operations_5, "expected": expected_5},
]
