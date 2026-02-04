part = 4

# Part 4: Target capacity limit
# Each target can hold at most maxConnectionsPerTarget connections.
# Skip full/offline targets. If all full, ignore the CONNECT (no log).

test_cases = [
    {
        # Capacity 1: each target holds 1 connection
        "num_targets": 2,
        "max_conns": 1,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            # c3 rejected - all full
        ],
    },
    {
        # Capacity 2: wraps around when first target is full
        "num_targets": 2,
        "max_conns": 2,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
            "CONNECT c4",
            "CONNECT c5",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c3, 1)",
            "(c4, 2)",
            # c5 rejected - all full
        ],
    },
    {
        # Disconnect frees capacity
        "num_targets": 2,
        "max_conns": 1,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
            "DISCONNECT c1",
            "CONNECT c4",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            # c3 rejected
            "(c4, 1)",
        ],
    },
    {
        # Capacity 3 with 3 targets
        "num_targets": 3,
        "max_conns": 2,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
            "CONNECT c4",
            "CONNECT c5",
            "CONNECT c6",
            "CONNECT c7",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c3, 3)",
            "(c4, 1)",
            "(c5, 2)",
            "(c6, 3)",
            # c7 rejected - all full
        ],
    },
]
