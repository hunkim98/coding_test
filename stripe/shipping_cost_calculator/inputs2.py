# Step 2: Volume Discounts (Tiered Pricing)
# Cost per unit changes based on quantity

part = 2

# Test case 1: US order with tiered laptop pricing
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
                {"minQuantity": 0, "maxQuantity": None, "cost": 550}
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {"minQuantity": 0, "maxQuantity": 2, "cost": 1000},
                {"minQuantity": 2, "maxQuantity": None, "cost": 900}
            ]
        }
    ]
}

# mouse: 20 × 550 = 11000
# laptop: (2 × 1000) + (3 × 900) = 2000 + 2700 = 4700
# total = 15700
expected_1 = 15700

# Test case 2: CA order with tiered pricing
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
                {"minQuantity": 0, "maxQuantity": None, "cost": 750}
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {"minQuantity": 0, "maxQuantity": 2, "cost": 1100},
                {"minQuantity": 2, "maxQuantity": None, "cost": 1000}
            ]
        }
    ]
}

# mouse: 20 × 750 = 15000
# laptop: (2 × 1100) + (3 × 1000) = 2200 + 3000 = 5200
# total = 20200
expected_2 = 20200

# Test case 3: Multiple tiers
order_3 = {
    "country": "US",
    "items": [
        {"product": "widget", "quantity": 25}
    ]
}

shipping_cost_3 = {
    "US": [
        {
            "product": "widget",
            "costs": [
                {"minQuantity": 0, "maxQuantity": 5, "cost": 100},   # First 5 at 100
                {"minQuantity": 5, "maxQuantity": 15, "cost": 80},   # Next 10 at 80
                {"minQuantity": 15, "maxQuantity": None, "cost": 60} # Rest at 60
            ]
        }
    ]
}

# widget: (5 × 100) + (10 × 80) + (10 × 60) = 500 + 800 + 600 = 1900
expected_3 = 1900

# Test case 4: Quantity fits exactly in first tier
order_4 = {
    "country": "US",
    "items": [
        {"product": "item", "quantity": 3}
    ]
}

shipping_cost_4 = {
    "US": [
        {
            "product": "item",
            "costs": [
                {"minQuantity": 0, "maxQuantity": 5, "cost": 200},
                {"minQuantity": 5, "maxQuantity": None, "cost": 150}
            ]
        }
    ]
}

# item: 3 × 200 = 600 (all in first tier)
expected_4 = 600

# Test case 5: Quantity exactly at tier boundary
order_5 = {
    "country": "US",
    "items": [
        {"product": "gadget", "quantity": 10}
    ]
}

shipping_cost_5 = {
    "US": [
        {
            "product": "gadget",
            "costs": [
                {"minQuantity": 0, "maxQuantity": 10, "cost": 50},
                {"minQuantity": 10, "maxQuantity": None, "cost": 40}
            ]
        }
    ]
}

# gadget: 10 × 50 = 500 (exactly fills first tier)
expected_5 = 500

test_cases = [
    {"order": order_1, "shipping_cost": shipping_cost_1, "expected": expected_1},
    {"order": order_2, "shipping_cost": shipping_cost_2, "expected": expected_2},
    {"order": order_3, "shipping_cost": shipping_cost_3, "expected": expected_3},
    {"order": order_4, "shipping_cost": shipping_cost_4, "expected": expected_4},
    {"order": order_5, "shipping_cost": shipping_cost_5, "expected": expected_5},
]
