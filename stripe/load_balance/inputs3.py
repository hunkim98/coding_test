part = 3

# Part 3: DISCONNECT support
# DISCONNECT removes a connection. No log entry for DISCONNECT.
# After DISCONNECT, the connId can be CONNECTed again as a new connection.

test_cases = [
    {
        # Basic disconnect then reconnect
        "num_targets": 2,
        "max_conns": 10,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "DISCONNECT c1",
            "CONNECT c3",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c3, 1)",
        ],
    },
    {
        # Disconnect non-existent connId - ignored
        "num_targets": 2,
        "max_conns": 10,
        "requests": [
            "CONNECT c1",
            "DISCONNECT c999",
            "CONNECT c2",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
        ],
    },
    {
        # Disconnect then reconnect same connId
        "num_targets": 3,
        "max_conns": 10,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "DISCONNECT c1",
            "CONNECT c1",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c1, 3)",
        ],
    },
    {
        # Multiple disconnects
        "num_targets": 2,
        "max_conns": 10,
        "requests": [
            "CONNECT c1",
            "CONNECT c2",
            "CONNECT c3",
            "DISCONNECT c1",
            "DISCONNECT c2",
            "CONNECT c4",
            "CONNECT c5",
        ],
        "expected": [
            "(c1, 1)",
            "(c2, 2)",
            "(c3, 1)",
            "(c4, 2)",
            "(c5, 1)",
        ],
    },
]
