"""
Worker Task Assignment

Step 1: Load balancing (least busy worker)
Step 2: Skill matching
Step 3: Account affinity (client history)
Step 4: Offline worker handling
"""

from typing import List, Dict, Optional, Union

# Change this import to test different steps
from inputs1 import test_cases, part
# from inputs2 import test_cases, part
# from inputs3 import test_cases, part
# from inputs4 import test_cases, part


def assign_tasks(
    workers: Union[List[str], List[Dict]],
    tasks: List[Dict],
    offlineEvents: Optional[List[Dict]] = None
) -> List[Dict]:
    """
    Assign tasks to workers based on rules for the current step.

    Args:
        workers: List of worker names (Step 1) or worker dicts (Steps 2-4)
        tasks: List of task dicts
        offlineEvents: Optional list of offline events (Step 4)

    Returns:
        List of assignment dicts with taskId and worker
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
        if part == 4:
            result = assign_tasks(
                tc["workers"],
                tc["tasks"],
                tc.get("offlineEvents", [])
            )
        else:
            result = assign_tasks(tc["workers"], tc["tasks"])

        expected = tc["expected"]
        passed = result == expected

        status = "✓" if passed else "✗"
        print(f"{status} Test {i + 1}")
        if not passed:
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")
        print()

        if not passed:
            all_passed = False

    return all_passed


if __name__ == "__main__":
    run_tests()
