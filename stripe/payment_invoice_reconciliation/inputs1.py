# Step 1: Match by ID
# Look for invoice ID in the payment memo

step = 1

test_cases = [
    {
        "payment": "payment-001, 1000, Paying off: inv-123",
        "invoices": [
            "inv-123, 2024-03-15, 1000",
            "inv-456, 2024-03-20, 1000",
            "inv-789, 2024-02-10, 500"
        ],
        "expected": "Payment payment-001 paid 1000 for invoice inv-123 due on 2024-03-15"
    },
    {
        "payment": "payment-002, 500, paying for: inv-456",
        "invoices": [
            "inv-123, 2024-03-15, 1000",
            "inv-456, 2024-03-20, 500"
        ],
        "expected": "Payment payment-002 paid 500 for invoice inv-456 due on 2024-03-20"
    },
    {
        "payment": "payment-003, 750, PAYING FOR: inv-999",
        "invoices": [
            "inv-123, 2024-03-15, 750"
        ],
        "expected": "Payment payment-003 could not be matched to any invoice"
        # inv-999 doesn't exist
    },
    {
        "payment": "payment-004, 100, Random memo text",
        "invoices": [
            "inv-123, 2024-03-15, 100"
        ],
        "expected": "Payment payment-004 could not be matched to any invoice"
        # No invoice ID in memo (for Step 1 only)
    },
]
