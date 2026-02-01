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
# from inputs1 import rates, test_cases, phase

# from inputs2 import rates, test_cases, phase

# from inputs3 import rates, test_cases, phase

from inputs4 import rates, test_cases, phase


class CurrencyNode:
    curr_str: str
    rates: {}

    def __init__(self, curr_str):
        self.curr_str = curr_str
        self.rates = {}

    def add_conn(self, conn_curr, rate):
        self.rates[conn_curr] = rate


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
        self.rates = defaultdict(lambda: {})
        self.collection = {}
        self.graph: list[list] = []  # For Phase 3-4: adjacency list
        self._parse_rates(rate_string)

    def _parse_rates(self, rate_string):
        infos = rate_string.split(",")
        for info in infos:
            args = info.split(":")
            cur1 = args[0]
            cur2 = args[1]
            cur1_to_cur2 = float(args[2])
            self.rates[cur1][cur2] = cur1_to_cur2
            self.rates[cur2][cur1] = 1.0 / cur1_to_cur2
            self.graph.append([cur1, cur2, cur1_to_cur2])
            self.graph.append([cur2, cur1, 1.0 / cur1_to_cur2])
        # construct a graph

    def get_direct_rate(self, from_curr: str, to_curr: str):
        if from_curr in self.rates:
            if to_curr in self.rates[from_curr]:
                return self.rates[from_curr][to_curr]
        return None

    def getRate(self, from_curr: str, to_curr: str) -> Optional[float]:
        """
        Get the exchange rate for a currency pair.
        """
        if from_curr == to_curr:
            return 1.0
        if from_curr not in self.rates or to_curr not in self.rates:
            return None
        cand_rate = self.get_direct_rate(from_curr=from_curr, to_curr=to_curr)
        if cand_rate is not None:
            return cand_rate
        # bellman ford

        V = len(set(self.rates.keys()))
        best = defaultdict(float)
        best[from_curr] = 1.0
        for _ in range(V - 1):
            new_best = best.copy()
            # we will do on each
            updated = False
            for u, v, r in self.graph:
                if best[u] == 0:
                    continue
                candidate = best[u] * r
                if candidate > new_best[v]:
                    new_best[v] = candidate
                    updated = True
            if not updated:
                break
            best = new_best
        if best[to_curr] == 0.0:
            return None
        return best[to_curr]


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
