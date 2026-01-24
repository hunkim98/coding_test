# Part 4: Timing matters
# Expected output: m1 50

part = 4

commands = [
    "1 INIT m1 0 5",
    "2 CREATE p1 m1 100",
    "3 CREATE p2 m1 50",
    "4 ATTEMPT p1",
    "5 ATTEMPT p2",
    "8 SUCCEED p1",
    "10 SUCCEED p2",
    "11 REFUND p1",
    "16 REFUND p2",
]
