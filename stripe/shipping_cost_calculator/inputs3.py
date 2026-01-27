# Step 3: Mixed Pricing Types
# Support both "incremental" (per unit) and "fixed" (flat fee) pricing

part = 3

# Test case 1: US order with fixed + incremental
order_1 = {
    "country": "US",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

shipping_cost_1 = {
    "US": [
        {
            "product": "mouse",
            "costs": [
                {"type": "incremental", "minQuantity": 0, "maxQuantity": None, "cost": 550}
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {"type": "fixed", "minQuantity": 0, "maxQuantity": 2, "cost": 1000},
                {"type": "incremental", "minQuantity": 2, "maxQuantity": None, "cost": 900}
            ]
        }
    ]
}

# mouse: 20 × 550 = 11000 (incremental)
# laptop: 1000 (fixed for first 2) + (3 × 900) = 1000 + 2700 = 3700
# total = 14700
expected_1 = 14700

# Test case 2: CA order with mixed pricing
order_2 = {
    "country": "CA",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

shipping_cost_2 = {
    "CA": [
        {
            "product": "mouse",
            "costs": [
                {"type": "incremental", "minQuantity": 0, "maxQuantity": None, "cost": 750}
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {"type": "fixed", "minQuantity": 0, "maxQuantity": 2, "cost": 1100},
                {"type": "incremental", "minQuantity": 2, "maxQuantity": None, "cost": 1000}
            ]
        }
    ]
}

# mouse: 20 × 750 = 15000 (incremental)
# laptop: 1100 (fixed for first 2) + (3 × 1000) = 1100 + 3000 = 4100
# total = 19100
expected_2 = 19100

# Test case 3: All fixed pricing
order_3 = {
    "country": "US",
    "items": [
        {"product": "subscription", "quantity": 10}
    ]
}

shipping_cost_3 = {
    "US": [
        {
            "product": "subscription",
            "costs": [
                {"type": "fixed", "minQuantity": 0, "maxQuantity": 5, "cost": 500},
                {"type": "fixed", "minQuantity": 5, "maxQuantity": None, "cost": 800}
            ]
        }
    ]
}

# subscription: 500 (fixed for 0-5) + 800 (fixed for 5+) = 1300
expected_3 = 1300

# Test case 4: Mixed tiers with all incremental
order_4 = {
    "country": "US",
    "items": [
        {"product": "item", "quantity": 15}
    ]
}

shipping_cost_4 = {
    "US": [
        {
            "product": "item",
            "costs": [
                {"type": "incremental", "minQuantity": 0, "maxQuantity": 5, "cost": 100},
                {"type": "incremental", "minQuantity": 5, "maxQuantity": 10, "cost": 80},
                {"type": "incremental", "minQuantity": 10, "maxQuantity": None, "cost": 60}
            ]
        }
    ]
}

# item: (5 × 100) + (5 × 80) + (5 × 60) = 500 + 400 + 300 = 1200
expected_4 = 1200

# Test case 5: Fixed tier not triggered (quantity too small)
order_5 = {
    "country": "US",
    "items": [
        {"product": "service", "quantity": 3}
    ]
}

shipping_cost_5 = {
    "US": [
        {
            "product": "service",
            "costs": [
                {"type": "fixed", "minQuantity": 0, "maxQuantity": 5, "cost": 200},
                {"type": "incremental", "minQuantity": 5, "maxQuantity": None, "cost": 50}
            ]
        }
    ]
}

# service: 200 (fixed for first tier, quantity 3 < 5)
# Second tier not reached
expected_5 = 200

# Test case 6: Alternating fixed and incremental
order_6 = {
    "country": "US",
    "items": [
        {"product": "complex", "quantity": 12}
    ]
}

shipping_cost_6 = {
    "US": [
        {
            "product": "complex",
            "costs": [
                {"type": "fixed", "minQuantity": 0, "maxQuantity": 3, "cost": 150},
                {"type": "incremental", "minQuantity": 3, "maxQuantity": 8, "cost": 40},
                {"type": "fixed", "minQuantity": 8, "maxQuantity": None, "cost": 100}
            ]
        }
    ]
}

# complex: 150 (fixed 0-3) + (5 × 40) (incremental 3-8) + 100 (fixed 8+)
# = 150 + 200 + 100 = 450
expected_6 = 450

test_cases = [
    {"order": order_1, "shipping_cost": shipping_cost_1, "expected": expected_1},
    {"order": order_2, "shipping_cost": shipping_cost_2, "expected": expected_2},
    {"order": order_3, "shipping_cost": shipping_cost_3, "expected": expected_3},
    {"order": order_4, "shipping_cost": shipping_cost_4, "expected": expected_4},
    {"order": order_5, "shipping_cost": shipping_cost_5, "expected": expected_5},
    {"order": order_6, "shipping_cost": shipping_cost_6, "expected": expected_6},
]
