"""
Factory Cost Optimizer

Part 1: Simple selection (no transport cost) - Greedy
Part 2: With transport costs - Try combinations
Part 3: N stages - Backtracking or DP
Part 4: Skip one stage - Try all skips
"""

from typing import List

# Change this import to test different parts
from inputs1 import stages, expected, part
# from inputs2 import stages, expected, part
# from inputs3 import stages, expected, part
# from inputs4 import stages, expected, part


def find_minimum_cost_part1(stages: List[List[List[int]]]) -> int:
    """
    Part 1: Find minimum cost when transport is free.
    Just pick the cheapest factory at each stage.

    Args:
        stages: List of stages, each containing [cost, position] pairs

    Returns:
        Minimum total building cost
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def find_minimum_cost_part2(stages: List[List[List[int]]]) -> int:
    """
    Part 2: Find minimum cost including transport.
    For 3 stages, try all combinations.

    Args:
        stages: List of stages, each containing [cost, position] pairs

    Returns:
        Minimum total cost (building + transport)
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def find_minimum_cost(stages: List[List[List[int]]]) -> int:
    """
    Part 3: Find minimum cost for N stages.
    Use backtracking or dynamic programming.

    Args:
        stages: List of stages, each containing [cost, position] pairs

    Returns:
        Minimum total cost (building + transport)
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def find_minimum_cost_skip_one(stages: List[List[List[int]]]) -> int:
    """
    Part 4: Find minimum cost when skipping exactly one stage.

    Args:
        stages: List of stages, each containing [cost, position] pairs

    Returns:
        Minimum total cost when one stage is skipped
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Test runner
if __name__ == "__main__":
    print(f"Testing Part {part}")
    print("=" * 50)
    print(f"Stages: {len(stages)}")
    for i, stage in enumerate(stages):
        print(f"  Stage {i}: {stage}")
    print()

    if part == 1:
        result = find_minimum_cost_part1(stages)
    elif part == 2:
        result = find_minimum_cost_part2(stages)
    elif part == 3:
        result = find_minimum_cost(stages)
    elif part == 4:
        result = find_minimum_cost_skip_one(stages)

    print(f"Result: {result}")
    if expected is not None:
        status = "✓" if result == expected else "✗"
        print(f"Expected: {expected} {status}")
