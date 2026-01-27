# Factory Cost Optimizer

## Problem Description

You are building a system to find the cheapest way to manufacture a product. The product is made in sequential stages, and for each stage you must choose one factory from multiple options.

Each factory has:
- **Building cost**: Cost to produce at this factory
- **Position**: Location on a railway line (integer)

**Total Cost = Building Costs + Transportation Costs**

Transportation cost between consecutive stages is the absolute distance: `|position_current - position_next|`

---

## Input Format

A list of stages, where each stage contains factory options as `[building_cost, position]` pairs:

```python
stages = [
    [[10, 0], [20, 5], [35, 2]],   # Stage 0: 3 factory options
    [[35, 1], [50, 3], [25, 0]],   # Stage 1: 3 factory options
    [[30, 4], [5, 2], [40, 0]]     # Stage 2: 3 factory options
]
```

---

## Part 1: Simple Selection (No Transport Cost)

### Description

Find the minimum total building cost when transportation is free (all factories at same position).

### Function Signature

```python
def find_minimum_cost(stages: List[List[List[int]]]) -> int:
```

### Sample Input

```python
stages = [
    [[10, 0], [20, 0], [35, 0]],   # Stage 0
    [[35, 0], [50, 0], [25, 0]],   # Stage 1
    [[30, 0], [5, 0], [40, 0]]     # Stage 2
]
```

### Sample Output

```python
find_minimum_cost(stages) == 40
# Stage 0: min = 10
# Stage 1: min = 25
# Stage 2: min = 5
# Total: 10 + 25 + 5 = 40
```

### Approach

- Greedy: Pick the cheapest factory at each stage
- Time: O(N × M) where N = stages, M = factories per stage

---

## Part 2: Adding Transport Costs

### Description

Include transportation costs based on distance between chosen factories.

Transport cost = `|position_i - position_{i+1}|`

### Sample Input

```python
stages = [
    [[100, 2], [50, 0], [30, 1]],   # Stage 0
    [[100, 1], [20, 2], [10, 5]],   # Stage 1
    [[10, 1], [12, 1], [5, 3]]      # Stage 2
]
```

### Sample Output

```python
find_minimum_cost(stages) == 51
# Best path:
# Stage 0: [30, 1] → cost=30, pos=1
# Stage 1: [10, 5] → cost=10, pos=5
# Stage 2: [5, 3]  → cost=5,  pos=3
#
# Building: 30 + 10 + 5 = 45
# Transport: |1-5| + |5-3| = 4 + 2 = 6
# Total: 45 + 6 = 51
```

### Approach

- Try all combinations (for small number of stages)
- Time: O(M^N) for brute force

---

## Part 3: Handling N Stages

### Description

Generalize to work with any number of stages using recursion or dynamic programming.

### Sample Input

```python
stages = [
    [[10, 0], [20, 2]],
    [[15, 1], [25, 3], [35, 0]],
    [[30, 2], [40, 1]],
    [[5, 0], [15, 2]],
    [[20, 1], [10, 3], [25, 0]]
]
```

### Sample Output

```python
find_minimum_cost(stages)  # Returns minimum total cost
```

### Approach

**Option 1: Backtracking**
```python
def backtrack(stage_idx, current_cost, prev_position):
    if stage_idx == n:
        return current_cost
    # Try each factory, recurse
```

**Option 2: Dynamic Programming**
- `dp[i][j]` = min cost to reach stage i using factory j
- Time: O(N × M²)

---

## Part 4: Skip One Stage

### Description

Find the minimum cost if you must skip **exactly one** stage. When skipping, transport cost is calculated between the stages before and after the gap.

### Function Signature

```python
def find_minimum_cost_skip_one(stages: List[List[List[int]]]) -> int:
```

### Sample Input

```python
stages = [
    [[10, 0], [20, 2]],     # Stage 0
    [[100, 5]],              # Stage 1 (expensive - consider skipping)
    [[15, 1], [25, 3]],      # Stage 2
    [[5, 2], [15, 0]]        # Stage 3
]
```

### Sample Output

```python
find_minimum_cost_skip_one(stages) == 32
# Skip Stage 1:
# Pick: [10, 0] → [15, 1] → [5, 2]
# Building: 10 + 15 + 5 = 30
# Transport: |0-1| + |1-2| = 1 + 1 = 2
# Total: 32
```

### Approach

- Try skipping each stage
- For each skip, compute min cost of remaining stages
- Return the minimum across all skip options

---

## Constraints

- 1 ≤ number of stages ≤ 20
- 1 ≤ factories per stage ≤ 100
- 0 ≤ building_cost ≤ 10^6
- 0 ≤ position ≤ 10^6
- All values are integers

---

## Notes

- Part 1 is a warm-up (greedy works)
- Part 2-3 require considering all combinations
- Part 4 builds on Part 3
- For large inputs, DP is more efficient than backtracking
- Early termination (pruning) can speed up backtracking
