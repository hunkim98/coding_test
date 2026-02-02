"""
Factory Cost Optimizer

Part 1: Simple selection (no transport cost) - Greedy
Part 2: With transport costs - Try combinations
Part 3: N stages - Backtracking or DP
Part 4: Skip one stage - Try all skips
"""

from typing import List

# Change this import to test different parts
# from inputs1 import stages, expected, part

from inputs2 import stages, expected, part

# from inputs3 import stages, expected, part
# from inputs4 import stages, expected, part


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
    total_cost = 0
    for stage in stages:
        min_cost = float("inf")
        min_pos = None
        for factory in stage:
            cost, pos = factory
            if cost < min_cost:
                min_cost = cost
                min_pos = pos
        total_cost += min_cost
        # print(min_cost, min_pos)
    return total_cost


# Test runner
if __name__ == "__main__":
    print(f"Testing Part {part}")
    print("=" * 50)
    print(f"Stages: {len(stages)}")
    for i, stage in enumerate(stages):
        print(f"  Stage {i}: {stage}")
    print()

    result = find_minimum_cost(stages)

    # if part == 1:
    #     result = find_minimum_cost_part1(stages)
    # elif part == 2:
    #     result = find_minimum_cost_part2(stages)
    # elif part == 3:
    #     result = find_minimum_cost(stages)
    # elif part == 4:
    #     result = find_minimum_cost_skip_one(stages)

    print(f"Result: {result}")
    if expected is not None:
        status = "✓" if result == expected else "✗"
        print(f"Expected: {expected} {status}")
