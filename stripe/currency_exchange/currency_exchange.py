"""
Currency Exchange System

Phase 1: Direct rate lookup (forward and reverse)
Phase 2: One intermediate currency
Phase 3: Best rate among multiple paths
Phase 4: Any path length (graph traversal)
"""

from typing import Optional, Dict, List, Set, Tuple
from collections import defaultdict

# Change this import to test different phases
from inputs1 import rates, test_cases, phase
# from inputs2 import rates, test_cases, phase
# from inputs3 import rates, test_cases, phase
# from inputs4 import rates, test_cases, phase


class CurrencyConverter:
    def __init__(self, rate_string: str):
        """
        Initialize the converter with a rate string.

        Args:
            rate_string: Comma-separated rates in format "FROM:TO:RATE,..."
        """
        # -----------------------------
        # Your implementation here
        # -----------------------------
        self.rates = {}  # For Phase 1-2: rates[from][to] = rate
        self.graph = defaultdict(list)  # For Phase 3-4: adjacency list
        self._parse_rates(rate_string)

    def _parse_rates(self, rate_string: str):
        """Parse the rate string into data structures."""
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass

    def getRate(self, from_curr: str, to_curr: str) -> Optional[float]:
        """
        Get the exchange rate from one currency to another.

        Args:
            from_curr: Source currency code
            to_curr: Target currency code

        Returns:
            Exchange rate as float, or None if not possible
        """
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass

    def _get_direct_rate(self, from_curr: str, to_curr: str) -> Optional[float]:
        """
        Phase 1: Get direct or reverse rate.

        Returns:
            Rate if direct connection exists, None otherwise
        """
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass

    def _get_one_step_rate(self, from_curr: str, to_curr: str) -> Optional[float]:
        """
        Phase 2: Get rate through one intermediate currency.

        Returns:
            Rate if one-step path exists, None otherwise
        """
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass

    def _get_best_rate_bfs(self, from_curr: str, to_curr: str) -> Optional[float]:
        """
        Phase 3-4: Find best rate using BFS/DFS.

        Returns:
            Best (maximum) rate among all paths, None if not connected
        """
        # -----------------------------
        # Your implementation here
        # -----------------------------
        pass


def run_tests(converter: CurrencyConverter, test_cases: List[Tuple]):
    """Run test cases and print results."""
    print(f"Testing Phase {phase}")
    print("=" * 50)

    for from_curr, to_curr, expected in test_cases:
        result = converter.getRate(from_curr, to_curr)

        if expected is None:
            passed = result is None
        else:
            passed = result is not None and abs(result - expected) < 0.0001

        status = "✓" if passed else "✗"
        print(f"{status} getRate({from_curr}, {to_curr})")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
        print()


# Test runner
if __name__ == "__main__":
    converter = CurrencyConverter(rates)
    run_tests(converter, test_cases)
