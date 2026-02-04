part = 2

# Part 2: Duplicate CONNECT handling
# If connId already exists, log the original assignment again without changing state.

test_cases = [
    {
        # Duplicate CONNECT returns original target
        "num_targets": 3,
        "max_conns": 10,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c1",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c1, 1)",
        ],
    },
    {
        # Duplicate does NOT advance nextTarget
        "num_targets": 3,
        "max_conns": 10,
        "requests": [
            "CONNECT c1",
            "CONNECT c1",
            "CONNECT c2",
        ],
        "expected": [
            "(c1, 1)",
            "(c1, 1)",
            "(c2, 2)",
        ],
    },
    {
        # Multiple duplicates
        "num_targets": 2,
        "max_conns": 10,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c1",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c1, 1)",
            "(c2, 2)",
            "(c1, 1)",
        ],
    },
]
