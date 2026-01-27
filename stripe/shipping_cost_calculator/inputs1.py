# Step 1: Simple Fixed Price
# Each product has one fixed price per unit

part = 1

# Test case 1: US order
order_1 = {
    "country": "US",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

shipping_cost_1 = {
    "US": [
        {"product": "mouse", "cost": 550},
        {"product": "laptop", "cost": 1000}
    ],
    "CA": [
        {"product": "mouse", "cost": 750},
        {"product": "laptop", "cost": 1100}
    ]
}

# mouse: 20 × 550 = 11000, laptop: 5 × 1000 = 5000, total = 16000
expected_1 = 16000

# Test case 2: CA order
order_2 = {
    "country": "CA",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

shipping_cost_2 = shipping_cost_1  # Same rules

# mouse: 20 × 750 = 15000, laptop: 5 × 1100 = 5500, total = 20500
expected_2 = 20500

# Test case 3: Single item
order_3 = {
    "country": "US",
    "items": [
        {"product": "keyboard", "quantity": 10}
    ]
}

shipping_cost_3 = {
    "US": [
        {"product": "keyboard", "cost": 200}
    ]
}

# keyboard: 10 × 200 = 2000
expected_3 = 2000

# Test case 4: Multiple products same country
order_4 = {
    "country": "UK",
    "items": [
        {"product": "phone", "quantity": 3},
        {"product": "tablet", "quantity": 2},
        {"product": "charger", "quantity": 5}
    ]
}

shipping_cost_4 = {
    "UK": [
        {"product": "phone", "cost": 1500},
        {"product": "tablet", "cost": 2000},
        {"product": "charger", "cost": 100}
    ]
}

# phone: 3 × 1500 = 4500, tablet: 2 × 2000 = 4000, charger: 5 × 100 = 500
# total = 9000
expected_4 = 9000

test_cases = [
    {"order": order_1, "shipping_cost": shipping_cost_1, "expected": expected_1},
    {"order": order_2, "shipping_cost": shipping_cost_2, "expected": expected_2},
    {"order": order_3, "shipping_cost": shipping_cost_3, "expected": expected_3},
    {"order": order_4, "shipping_cost": shipping_cost_4, "expected": expected_4},
]
