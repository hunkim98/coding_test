# Part 2: Memory Optimization
# Efficient cleanup of old timestamps

part = 2

# Test case 1: Cleanup old entries
config_1 = {"max_requests": 3, "window_seconds": 10}
operations_1 = [
    ("hit", "user_1", 1),
    ("hit", "user_1", 2),
    ("hit", "user_1", 3),
    ("allowed", "user_1", 5),   # 3 hits, False
    ("allowed", "user_1", 15),  # All old, True (and cleaned up)
    ("get_memory", "user_1"),   # Should have 0 entries after cleanup
]
expected_1 = [False, True, 0]

# Test case 2: Partial cleanup
config_2 = {"max_requests": 5, "window_seconds": 10}
operations_2 = [
    ("hit", "user", 1),
    ("hit", "user", 5),
    ("hit", "user", 8),
    ("hit", "user", 12),
    ("get_memory", "user"),     # 4 entries
    ("allowed", "user", 15),    # t=1,5 outside window, 2 remain
    ("get_memory", "user"),     # Should have 2 entries (t=8,12)
]
expected_2 = [4, True, 2]

# Test case 3: Key deletion when empty
config_3 = {"max_requests": 2, "window_seconds": 5}
operations_3 = [
    ("hit", "temp_user", 1),
    ("hit", "temp_user", 2),
    ("key_exists", "temp_user"),  # True
    ("allowed", "temp_user", 100), # Way past window
    ("key_exists", "temp_user"),  # Should be False (key deleted)
]
expected_3 = [True, True, False]

# Test case 4: Multiple users cleanup
config_4 = {"max_requests": 2, "window_seconds": 10}
operations_4 = [
    ("hit", "alice", 1),
    ("hit", "bob", 1),
    ("hit", "charlie", 1),
    ("get_total_keys",),        # 3 keys
    ("allowed", "alice", 20),   # Cleans alice
    ("allowed", "bob", 20),     # Cleans bob
    ("allowed", "charlie", 20), # Cleans charlie
    ("get_total_keys",),        # 0 keys (all cleaned)
]
expected_4 = [3, True, True, True, 0]

test_cases = [
    {"config": config_1, "operations": operations_1, "expected": expected_1},
    {"config": config_2, "operations": operations_2, "expected": expected_2},
    {"config": config_3, "operations": operations_3, "expected": expected_3},
    {"config": config_4, "operations": operations_4, "expected": expected_4},
]
