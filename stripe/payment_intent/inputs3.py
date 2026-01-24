# Part 3: Accepting failure
# Expected output: m1 50

part = 3

commands = [
    "INIT m1 0",
    "CREATE p1 m1 50",
    "ATTEMPT p1",
    "FAIL p1",
    "ATTEMPT p1",
    "SUCCEED p1",
    "CREATE p2 m1 100",
    "ATTEMPT p2",
    "SUCCEED p2",
    "REFUND p2",
]
