part = 5

# Part 5: SHUTDOWN with eviction and reassignment
# SHUTDOWN targetId: mark offline, evict all connections in assignment order,
# try to reassign each using routing policy. Log successful reassignments.

test_cases = [
    {
        # Example from problem description
        "num_targets": 2,
        "max_conns": 2,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "SHUTDOWN 1",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c1, 2)",
        ],
    },
    {
        # Shutdown target with multiple connections - reassign in order
        "num_targets": 3,
        "max_conns": 3,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
            "CONNECT c4",
            "CONNECT c5",
            "SHUTDOWN 1",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c3, 3)",
            "(c4, 1)",
            "(c5, 2)",
            # SHUTDOWN 1: evicts c1 (assigned first), then c4
            "(c1, 3)",
            "(c4, 2)",
        ],
    },
    {
        # Shutdown when reassignment target is full - drop silently
        "num_targets": 2,
        "max_conns": 1,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "SHUTDOWN 1",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            # SHUTDOWN 1: evicts c1, target 2 is full -> dropped
        ],
    },
    {
        # Shutdown all targets
        "num_targets": 2,
        "max_conns": 2,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "SHUTDOWN 1",
            "SHUTDOWN 2",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c1, 2)",
            # SHUTDOWN 2: evicts c2, c1. No online targets -> all dropped
        ],
    },
    {
        # Connect after shutdown
        "num_targets": 3,
        "max_conns": 2,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
            "SHUTDOWN 1",
            "CONNECT c4",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c3, 3)",
            # SHUTDOWN 1: evicts c1, reassign to target 2
            "(c1, 2)",
            # CONNECT c4: nextTarget should continue from routing, target 1 offline
            "(c4, 3)",
        ],
    },
    {
        # Disconnect before shutdown
        "num_targets": 2,
        "max_conns": 2,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
            "DISCONNECT c1",
            "SHUTDOWN 1",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c3, 1)",
            # DISCONNECT c1: frees slot on target 1
            # SHUTDOWN 1: evicts c3 (only remaining on target 1)
            "(c3, 2)",
        ],
    },
]
