# Step 3: Fuzzy Match (Forgiveness)
# Allow matching within a tolerance range

step = 3

test_cases = [
    {
        # Exact match beats fuzzy match
        "payment": "payment-001, 98, Customer payment",
        "invoices": [
            "inv-100, 2024-03-15, 100",
            "inv-200, 2024-02-20, 98",
            "inv-300, 2024-01-10, 102"
        ],
        "forgiveness": 5,
        "expected": "Payment payment-001 paid 98 for invoice inv-200 due on 2024-02-20"
    },
    {
        # Fuzzy match - earliest date wins
        "payment": "payment-002, 95, Customer payment",
        "invoices": [
            "inv-100, 2024-03-15, 100",
            "inv-300, 2024-01-10, 97"
        ],
        "forgiveness": 5,
        "expected": "Payment payment-002 paid 95 for invoice inv-300 due on 2024-01-10"
        # Both within range [90, 100], inv-300 is earlier
    },
    {
        # Outside forgiveness range
        "payment": "payment-003, 90, Payment",
        "invoices": [
            "inv-100, 2024-03-15, 100"
        ],
        "forgiveness": 5,
        "expected": "Payment payment-003 could not be matched to any invoice"
        # 100 is outside [85, 95]
    },
    {
        # Exact boundary of forgiveness
        "payment": "payment-004, 95, Payment",
        "invoices": [
            "inv-100, 2024-03-15, 100"
        ],
        "forgiveness": 5,
        "expected": "Payment payment-004 paid 95 for invoice inv-100 due on 2024-03-15"
        # 100 is exactly at boundary [90, 100]
    },
    {
        # ID match still has highest priority
        "payment": "payment-005, 95, Paying for: inv-200",
        "invoices": [
            "inv-100, 2024-01-01, 95",   # Exact amount match
            "inv-200, 2024-03-15, 1000"  # ID match
        ],
        "forgiveness": 5,
        "expected": "Payment payment-005 paid 95 for invoice inv-200 due on 2024-03-15"
    },
]
