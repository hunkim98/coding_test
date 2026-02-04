part = 1

# Part 1: Basic gap filling
# Input intervals are already sorted, no overlaps, no merging needed.
# Just fill the gaps.

test_cases = [
    {
        # Gaps at beginning, middle, and end
        "bin": "424242",
        "intervals": [
            "4242420500000000,4242421000000000,visa",
            "4242425000000000,4242428000000000,mastercard",
        ],
        "expected": [
            "4242420000000000,4242420499999999,unknown",
            "4242420500000000,4242421000000000,visa",
            "4242421000000001,4242424999999999,unknown",
            "4242425000000000,4242428000000000,mastercard",
            "4242428000000001,4242429999999999,unknown",
        ],
    },
    {
        # Gap only at end
        "bin": "424242",
        "intervals": [
            "4242420000000000,4242425000000000,visa",
        ],
        "expected": [
            "4242420000000000,4242425000000000,visa",
            "4242425000000001,4242429999999999,unknown",
        ],
    },
    {
        # Gap only at beginning
        "bin": "424242",
        "intervals": [
            "4242425000000000,4242429999999999,mastercard",
        ],
        "expected": [
            "4242420000000000,4242424999999999,unknown",
            "4242425000000000,4242429999999999,mastercard",
        ],
    },
    {
        # Multiple brands, gap in middle only
        "bin": "424242",
        "intervals": [
            "4242420000000000,4242423000000000,visa",
            "4242427000000000,4242429999999999,mastercard",
        ],
        "expected": [
            "4242420000000000,4242423000000000,visa",
            "4242423000000001,4242426999999999,unknown",
            "4242427000000000,4242429999999999,mastercard",
        ],
    },
]
