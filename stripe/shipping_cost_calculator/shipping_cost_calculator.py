"""
Shipping Cost Calculator

Step 1: Simple fixed price per unit
Step 2: Volume discounts (tiered pricing)
Step 3: Mixed pricing types (incremental vs fixed)
"""

from typing import Dict, List

# Change this import to test different steps
from inputs1 import test_cases, part
# from inputs2 import test_cases, part
# from inputs3 import test_cases, part


def calculate_shipping_cost(order: Dict, shipping_cost: Dict) -> int:
    """
    Calculate total shipping cost for an order.

    Args:
        order: Dict with "country" and "items" (list of product/quantity)
        shipping_cost: Dict mapping country to product pricing rules

    Returns:
        Total shipping cost as integer
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Test runner
def run_tests():
    print(f"Testing Step {part}")
    print("=" * 60)

    all_passed = True
    for i, tc in enumerate(test_cases):
        result = calculate_shipping_cost(tc["order"], tc["shipping_cost"])
        expected = tc["expected"]
        passed = result == expected

        status = "✓" if passed else "✗"
        print(f"{status} Test {i + 1}")
        if not passed:
            print(f"   Order: {tc['order']}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")
        print()

        if not passed:
            all_passed = False

    return all_passed


if __name__ == "__main__":
    run_tests()
