part = 1

# Part 1: Basic CONNECT routing
# No duplicates, no disconnect, no capacity limit, all targets online.
# Round-robin assignment using nextTarget pointer.

test_cases = [
    {
        # Basic: 3 connections across 3 targets
        "num_targets": 3,
        "max_conns": 10,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c3, 3)",
        ],
    },
    {
        # Round-robin wraps around
        "num_targets": 2,
        "max_conns": 10,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
            "CONNECT c4",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c3, 1)",
            "(c4, 2)",
        ],
    },
    {
        # Single target
        "num_targets": 1,
        "max_conns": 10,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 1)",
            "(c3, 1)",
        ],
    },
    {
        # 5 connections across 3 targets
        "num_targets": 3,
        "max_conns": 10,
        "requests": [
            "CONNECT a",
            "CONNECT b",
            "CONNECT c",
            "CONNECT d",
            "CONNECT e",
        ],
        "expected": [
            "(a, 1)",
            "(b, 2)",
            "(c, 3)",
            "(d, 1)",
            "(e, 2)",
        ],
    },
]
