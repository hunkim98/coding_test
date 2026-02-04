part = 3

# Part 3: Edge cases
# Empty intervals, full coverage, single card number intervals, different BINs.

test_cases = [
    {
        # No intervals at all - entire range is unknown
        "bin": "424242",
        "intervals": [],
        "expected": [
            "4242420000000000,4242429999999999,unknown",
        ],
    },
    {
        # Full coverage - no gaps to fill
        "bin": "424242",
        "intervals": [
            "4242420000000000,4242429999999999,visa",
        ],
        "expected": [
            "4242420000000000,4242429999999999,visa",
        ],
    },
    {
        # Single card number interval (start == end)
        "bin": "424242",
        "intervals": [
            "4242425000000000,4242425000000000,amex",
        ],
        "expected": [
            "4242420000000000,4242424999999999,unknown",
            "4242425000000000,4242425000000000,amex",
            "4242425000000001,4242429999999999,unknown",
        ],
    },
    {
        # Different BIN, gap at end only
        "bin": "555555",
        "intervals": [
            "5555550000000000,5555554999999999,mastercard",
        ],
        "expected": [
            "5555550000000000,5555554999999999,mastercard",
            "5555555000000000,5555559999999999,unknown",
        ],
    },
    {
        # Many small intervals with gaps everywhere
        "bin": "100000",
        "intervals": [
            "1000001000000000,1000001999999999,visa",
            "1000005000000000,1000005999999999,mastercard",
            "1000008000000000,1000008999999999,amex",
        ],
        "expected": [
            "1000000000000000,1000000999999999,unknown",
            "1000001000000000,1000001999999999,visa",
            "1000002000000000,1000004999999999,unknown",
            "1000005000000000,1000005999999999,mastercard",
            "1000006000000000,1000007999999999,unknown",
            "1000008000000000,1000008999999999,amex",
            "1000009000000000,1000009999999999,unknown",
        ],
    },
]
