"""
Subscription Email Scheduler

Part 1: Schedule emails based on subscription timeline
Part 2: Handle plan changes
Part 3: Handle renewals with recalculation
"""

from typing import Dict, List, Optional

# Change this import to test different parts
from inputs1 import test_cases, part
# from inputs2 import test_cases, part
# from inputs3 import test_cases, part


def send_emails(
    user_accounts: List[Dict],
    send_schedule: Dict,
    changes: Optional[List[Dict]] = None
) -> str:
    """
    Generate email notifications for subscription events.

    Args:
        user_accounts: List of user subscription info
        send_schedule: Dict mapping event keys to message types
        changes: Optional list of plan changes and/or renewals

    Returns:
        Multiline string of email events in chronological order
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
        if part == 1:
            result = send_emails(
                tc["user_accounts"],
                tc["send_schedule"]
            )
        else:
            result = send_emails(
                tc["user_accounts"],
                tc["send_schedule"],
                tc.get("changes", [])
            )

        expected = tc["expected"]
        passed = result == expected

        status = "✓" if passed else "✗"
        print(f"{status} Test {i + 1}")
        if not passed:
            print(f"   Expected:\n{expected}")
            print(f"   Got:\n{result}")
        print()

        if not passed:
            all_passed = False

    return all_passed


if __name__ == "__main__":
    run_tests()
