# Shipping Cost Calculator

## Problem Description

Write code to calculate shipping costs for an online store. The cost depends on the country and the type of product. This problem has three steps that progressively increase in complexity.

---

## Data Format

### Order Object

```python
{
    "country": "US",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}
```

### Shipping Cost Rules

A dictionary containing price rules for each country and product. The format varies by step.

---

## Step 1: Simple Fixed Price

### Task

Write a function `calculate_shipping_cost(order, shipping_cost)` that calculates the total cost when every product has one fixed price per unit.

### Input Format

```python
shipping_cost = {
    "US": [
        {"product": "mouse", "cost": 550},
        {"product": "laptop", "cost": 1000}
    ],
    "CA": [
        {"product": "mouse", "cost": 750},
        {"product": "laptop", "cost": 1100}
    ]
}
```

### Example

```
Order: {"country": "US", "items": [{"product": "mouse", "quantity": 20}, {"product": "laptop", "quantity": 5}]}

Calculation:
  mouse:  20 × 550  = 11000
  laptop:  5 × 1000 =  5000
  Total: 16000

Output: 16000
```

### Requirements

- Handle orders with multiple different products
- Use correct prices for the specific country
- Return the answer as an integer

---

## Step 2: Volume Discounts (Tiered Pricing)

### Task

Update your function to handle "tiered pricing" where the cost per unit changes based on quantity.

Each tier has:
- `minQuantity`: Start of the range (inclusive)
- `maxQuantity`: End of the range (exclusive), or `None` for unlimited

### Input Format

```python
shipping_cost = {
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
                {"minQuantity": 3, "maxQuantity": None, "cost": 900}
            ]
        }
    ]
}
```

### Example

```
Order: {"country": "US", "items": [{"product": "mouse", "quantity": 20}, {"product": "laptop", "quantity": 5}]}

Calculation:
  mouse:  20 × 550 = 11000 (single tier)
  laptop: (2 × 1000) + (3 × 900) = 2000 + 2700 = 4700
  Total: 15700

Output: 15700
```

### Tier Logic

- Process tiers in order from lowest to highest quantity
- Range is `[minQuantity, maxQuantity)` (includes min, excludes max)
- `maxQuantity: None` means unlimited
- Calculate cost for each tier separately and sum them

---

## Step 3: Mixed Pricing Types

### Task

Support two different pricing types within tiers:

- `incremental`: Charge per unit (Quantity × Cost)
- `fixed`: Charge one flat fee for the entire tier

### Input Format

```python
shipping_cost = {
    "US": [
        {
            "product": "laptop",
            "costs": [
                {"type": "fixed", "minQuantity": 0, "maxQuantity": 2, "cost": 1000},
                {"type": "incremental", "minQuantity": 3, "maxQuantity": None, "cost": 900}
            ]
        }
    ]
}
```

### Example

```
Order: {"country": "US", "items": [{"product": "laptop", "quantity": 5}]}

Calculation:
  laptop: 1000 (fixed fee for first 2) + (3 × 900) = 1000 + 2700 = 3700

Output: 3700
```

### Type Rules

- `fixed`: Add the cost once if ANY items fall into this tier
- `incremental`: Multiply quantity in tier × cost
- A product can mix both types across different tiers

---

## Constraints

- Country codes are valid strings (e.g., "US", "CA")
- Product names are non-empty strings
- Quantities are positive integers
- Costs are positive integers (representing cents)
- Tiers are sorted by `minQuantity` in ascending order
- Tier ranges do not overlap

---

## Test Format

```python
def calculate_shipping_cost(order: dict, shipping_cost: dict) -> int:
    pass
```

Each test case provides an `order`, `shipping_cost` rules, and `expected` result.
