# Part 1: Good intentions
# Expected output: m1 50, m2 10

part = 1

commands = [
    "INIT m1 0",
    "INIT m2 10",
    "CREATE p1 m1 50",
    "ATTEMPT p1",
    "SUCCEED p1",
    "CREATE p2 m2 100",
    "ATTEMPT p2",
]
