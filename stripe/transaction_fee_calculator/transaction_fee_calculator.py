"""
Transaction Fee Calculator

Part 1: Basic fee calculation from CSV
Part 2: Conditional rules (status, regional rates)
Part 3: Volume-based discounts
"""

from collections import defaultdict
from typing import Dict, Optional

# Change this import to test different parts
from inputs1 import test_cases, part
# from inputs2 import test_cases, part
# from inputs3 import test_cases, part


def calculate_fees(csv_data: str, country_fees: Optional[Dict] = None) -> str:
    """
    Calculate transaction fees from CSV data.

    Args:
        csv_data: CSV string with transaction data
        country_fees: Optional dict of country-specific fee rates (Part 3)

    Returns:
        CSV string with id, transaction_type, payment_provider, fee
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Test runner
def run_tests():
    print(f"Testing Part {part}")
    print("=" * 60)

    all_passed = True
    for i, tc in enumerate(test_cases):
        if part == 3:
            result = calculate_fees(tc["csv_data"], tc["country_fees"])
        else:
            result = calculate_fees(tc["csv_data"])

        expected = tc["expected"]
        passed = result == expected

        status = "✓" if passed else "✗"
        print(f"{status} Test {i + 1}")
        if not passed:
            # Show first few lines of difference
            result_lines = result.split('\n') if result else []
            expected_lines = expected.split('\n')
            print(f"   Expected lines: {len(expected_lines)}")
            print(f"   Got lines:      {len(result_lines)}")
            for j, (e, r) in enumerate(zip(expected_lines[:5], result_lines[:5])):
                if e != r:
                    print(f"   Line {j}: expected '{e}' got '{r}'")
        print()

        if not passed:
            all_passed = False

    return all_passed


if __name__ == "__main__":
    run_tests()
