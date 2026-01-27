# Step 2: Match by Amount
# If no ID in memo, match by exact amount (earliest date wins)

step = 2

test_cases = [
    {
        "payment": "payment-001, 500, Monthly subscription",
        "invoices": [
            "inv-001, 2024-03-22, 1000",
            "inv-002, 2024-02-05, 500",
            "inv-003, 2024-03-01, 500",
            "inv-004, 2024-01-15, 500"
        ],
        "expected": "Payment payment-001 paid 500 for invoice inv-004 due on 2024-01-15"
        # inv-004 has earliest date among 500-amount invoices
    },
    {
        "payment": "payment-002, 1000, Payment",
        "invoices": [
            "inv-100, 2024-03-15, 1000",
            "inv-200, 2024-03-15, 500"
        ],
        "expected": "Payment payment-002 paid 1000 for invoice inv-100 due on 2024-03-15"
    },
    {
        "payment": "payment-003, 750, Payment",
        "invoices": [
            "inv-100, 2024-03-15, 1000",
            "inv-200, 2024-03-15, 500"
        ],
        "expected": "Payment payment-003 could not be matched to any invoice"
        # No invoice with amount 750
    },
    {
        # ID match still takes priority
        "payment": "payment-004, 500, Paying for: inv-100",
        "invoices": [
            "inv-100, 2024-03-15, 1000",  # ID matches but amount differs
            "inv-200, 2024-02-10, 500"     # Amount matches
        ],
        "expected": "Payment payment-004 paid 500 for invoice inv-100 due on 2024-03-15"
        # ID match wins over amount match
    },
]
