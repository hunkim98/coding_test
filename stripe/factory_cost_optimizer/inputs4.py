# Part 4: Skip One Stage
# Expected output: 32
#
# Skip Stage 1 (the expensive one):
# Pick: [10, 0] → skip → [15, 1] → [5, 2]
# Building: 10 + 15 + 5 = 30
# Transport: |0-1| + |1-2| = 1 + 1 = 2
# Total: 30 + 2 = 32

part = 4

stages = [
    [[10, 0], [20, 2]],     # Stage 0
    [[100, 5]],              # Stage 1 (expensive - skip this)
    [[15, 1], [25, 3]],      # Stage 2
    [[5, 2], [15, 0]]        # Stage 3
]

expected = 32
