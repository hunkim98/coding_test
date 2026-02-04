part = 2

# Part 2: Unsorted input + merge overlapping/adjacent intervals with same brand
# Now you must sort the intervals first and merge where appropriate.

test_cases = [
    {
        # Unsorted input - should produce same result as Part 1 test 1
        "bin": "424242",
        "intervals": [
            "4242425000000000,4242428000000000,mastercard",
            "4242420500000000,4242421000000000,visa",
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
        # Adjacent intervals with same brand should merge
        "bin": "424242",
        "intervals": [
            "4242420000000000,4242424999999999,visa",
            "4242425000000000,4242429999999999,visa",
        ],
        "expected": [
            "4242420000000000,4242429999999999,visa",
        ],
    },
    {
        # Overlapping intervals with same brand should merge
        "bin": "424242",
        "intervals": [
            "4242420000000000,4242425000000000,visa",
            "4242424000000000,4242429999999999,visa",
        ],
        "expected": [
            "4242420000000000,4242429999999999,visa",
        ],
    },
    {
        # Adjacent intervals with different brands should NOT merge
        "bin": "424242",
        "intervals": [
            "4242420000000000,4242424999999999,visa",
            "4242425000000000,4242429999999999,mastercard",
        ],
        "expected": [
            "4242420000000000,4242424999999999,visa",
            "4242425000000000,4242429999999999,mastercard",
        ],
    },
    {
        # Multiple unsorted, some adjacent same-brand
        "bin": "555555",
        "intervals": [
            "5555557000000000,5555559999999999,amex",
            "5555550000000000,5555552999999999,visa",
            "5555553000000000,5555554999999999,visa",
        ],
        "expected": [
            "5555550000000000,5555554999999999,visa",
            "5555555000000000,5555556999999999,unknown",
            "5555557000000000,5555559999999999,amex",
        ],
    },
]
