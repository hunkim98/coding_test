"""
Rate Limiter

Part 1: Basic sliding window rate limiting
Part 2: Memory optimization with cleanup
Part 3: Handle edge cases (burst, out-of-order, gaps)
Part 4: Thread safety with atomic check-and-hit
"""

from collections import defaultdict, deque
import threading
from typing import List, Tuple, Any

# Change this import to test different parts
from inputs1 import test_cases, part
# from inputs2 import test_cases, part
# from inputs3 import test_cases, part
# from inputs4 import test_cases, part


class RateLimiter:
    """Basic rate limiter for Parts 1-3."""

    def __init__(self, max_requests: int, window_seconds: int):
        """
        Initialize the rate limiter.

        Args:
            max_requests: Maximum requests allowed in the window
            window_seconds: Size of the time window in seconds
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        # -----------------------------
        # Your implementation here
        # -----------------------------

    def hit(self, key: str, timestamp: int) -> None:
        """Record a request for a key at a specific time."""
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass

    def allowed(self, key: str, timestamp: int) -> bool:
        """
        Check if the key is allowed to make a request.

        Returns:
            True if hits in current window < max_requests, False otherwise
        """
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass

    # Part 2: Memory optimization helpers
    def get_memory(self, key: str) -> int:
        """Return the number of stored timestamps for a key."""
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass

    def key_exists(self, key: str) -> bool:
        """Check if a key exists in storage."""
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass

    def get_total_keys(self) -> int:
        """Return the total number of keys in storage."""
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass


class ThreadSafeRateLimiter(RateLimiter):
    """Thread-safe rate limiter for Part 4."""

    def __init__(self, max_requests: int, window_seconds: int):
        super().__init__(max_requests, window_seconds)
        # -----------------------------
        # Your implementation here
        # Add locking mechanism
        # -----------------------------

    def check_and_hit(self, key: str, timestamp: int) -> bool:
        """
        Atomically check limit and record hit.

        Returns:
            True if allowed (and hit recorded), False otherwise
        """
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass


def run_operations(limiter, operations: List[Tuple]) -> List[Any]:
    """Execute operations and collect results."""
    results = []
    for op in operations:
        if op[0] == "hit":
            limiter.hit(op[1], op[2])
        elif op[0] == "allowed":
            results.append(limiter.allowed(op[1], op[2]))
        elif op[0] == "check_and_hit":
            results.append(limiter.check_and_hit(op[1], op[2]))
        elif op[0] == "get_memory":
            results.append(limiter.get_memory(op[1]))
        elif op[0] == "key_exists":
            results.append(limiter.key_exists(op[1]))
        elif op[0] == "get_total_keys":
            results.append(limiter.get_total_keys())
    return results


# Test runner
def run_tests():
    print(f"Testing Part {part}")
    print("=" * 60)

    all_passed = True
    for i, tc in enumerate(test_cases):
        config = tc["config"]

        if part == 4:
            limiter = ThreadSafeRateLimiter(
                config["max_requests"], config["window_seconds"]
            )
        else:
            limiter = RateLimiter(
                config["max_requests"], config["window_seconds"]
            )

        result = run_operations(limiter, tc["operations"])
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
