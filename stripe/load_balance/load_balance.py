"""
Stripe OA - Jupyter Server Connection Management (Load Balancer)

Parts:
- Part 1: Basic CONNECT routing (round-robin)
- Part 2: Duplicate CONNECT handling
- Part 3: DISCONNECT support
- Part 4: Target capacity limit
- Part 5: SHUTDOWN with eviction and reassignment
"""

from typing import List
from inputs1 import test_cases, part


def process_requests(
    num_targets: int,
    max_connections_per_target: int,
    requests: List[str],
) -> List[str]:
    """
    Process a list of CONNECT/DISCONNECT/SHUTDOWN requests and return
    a log of connection assignment events.

    Each log entry: "(connId, targetId)"

    Routing policy:
    - Maintain nextTarget pointer (starts at 1)
    - Scan circularly for first online, non-full target
    - Update nextTarget = selectedTarget + 1 after assignment
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def run_tests():
    print(f"Testing Part {part}")
    for i, tc in enumerate(test_cases):
        result = process_requests(tc["num_targets"], tc["max_conns"], tc["requests"])
        passed = result == tc["expected"]
        status = "PASS" if passed else "FAIL"
        print(f"  {status}: Test {i + 1}")
        if not passed:
            print(f"    Expected: {tc['expected']}")
            print(f"    Got:      {result}")


if __name__ == "__main__":
    run_tests()
