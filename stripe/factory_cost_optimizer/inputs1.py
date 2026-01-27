# Part 1: Simple Selection (No Transport Cost)
# Expected output: 40
# Stage 0: min = 10
# Stage 1: min = 25
# Stage 2: min = 5
# Total: 10 + 25 + 5 = 40

part = 1

stages = [
    [[10, 0], [20, 0], [35, 0]],   # Stage 0
    [[35, 0], [50, 0], [25, 0]],   # Stage 1
    [[30, 0], [5, 0], [40, 0]]     # Stage 2
]

expected = 40
