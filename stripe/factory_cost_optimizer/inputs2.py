# Part 2: Adding Transport Costs
# Expected output: 51
#
# Best path:
# Stage 0: [30, 1] → cost=30, pos=1
# Stage 1: [10, 5] → cost=10, pos=5
# Stage 2: [5, 3]  → cost=5,  pos=3
#
# Building: 30 + 10 + 5 = 45
# Transport: |1-5| + |5-3| = 4 + 2 = 6
# Total: 45 + 6 = 51

part = 2

stages = [
    [[100, 2], [50, 0], [30, 1]],   # Stage 0
    [[100, 1], [20, 2], [10, 5]],   # Stage 1
    [[10, 1], [12, 1], [5, 3]]      # Stage 2
]

expected = 51
