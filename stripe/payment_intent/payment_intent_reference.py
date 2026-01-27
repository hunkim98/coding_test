"""
Reference solution - written as if solving in 60 min timed test.

Strategy:
- Part 1 (~10 min): Get basic INIT/CREATE/ATTEMPT/SUCCEED working
- Part 2 (~5 min): Add UPDATE - quick, just one more case
- Part 3 (~10 min): Add FAIL and REFUND
- Part 4 (~15 min): Add timestamps and timeout logic
- Buffer (~20 min): Debug, edge cases, testing

Key insight: Don't over-engineer. Use simple dicts, add features incrementally.
"""

from typing import List

# Status constants - simple integers, fast to type
REQUIRE_ACTION = 0
PROCESSING = 1
SUCCEEDED = 2
REFUNDED = 3


def execute(commands: List[str], part: int) -> List[str]:
    # Simple dicts - don't overthink data structures
    merchants = {}  # mid -> {"balance": int, "payments": [], "timeout": int|None}
    payments = (
        {}
    )  # pid -> {"mid": str, "amount": int, "status": int, "succeed_time": int}

    # Detect timed vs non-timed format
    has_time = commands[0].split()[0].isdigit()

    for cmd in commands:
        parts = cmd.split()

        if has_time:
            time, action = int(parts[0]), parts[1]
            args = parts[2:]
        else:
            time, action = None, parts[0]
            args = parts[1:]

        # INIT: mid, balance, [timeout]
        if action == "INIT":
            mid, balance = args[0], int(args[1])
            timeout = int(args[2]) if len(args) > 2 else None
            # Negative timeout = unlimited
            if timeout is not None and timeout < 0:
                timeout = None
            merchants[mid] = {"balance": balance, "payments": [], "timeout": timeout}

        # CREATE: pid, mid, amount
        elif action == "CREATE":
            pid, mid, amount = args[0], args[1], int(args[2])
            # Validate: merchant exists, payment doesn't exist, amount > 0
            if mid not in merchants:
                continue
            if pid in payments:
                continue
            if amount <= 0:
                continue
            payments[pid] = {
                "mid": mid,
                "amount": amount,
                "status": REQUIRE_ACTION,
                "succeed_time": None,
            }
            merchants[mid]["payments"].append(pid)

        # ATTEMPT: pid
        elif action == "ATTEMPT":
            pid = args[0]
            if pid not in payments:
                continue
            if payments[pid]["status"] != REQUIRE_ACTION:
                continue
            payments[pid]["status"] = PROCESSING

        # SUCCEED: pid
        elif action == "SUCCEED":
            pid = args[0]
            if pid not in payments:
                continue
            if payments[pid]["status"] != PROCESSING:
                continue
            payments[pid]["status"] = SUCCEEDED
            payments[pid]["succeed_time"] = time  # For Part 4

        # FAIL: pid (Part 3)
        elif action == "FAIL":
            pid = args[0]
            if pid not in payments:
                continue
            if payments[pid]["status"] != PROCESSING:
                continue
            payments[pid]["status"] = REQUIRE_ACTION  # Back to start

        # UPDATE: pid, new_amount (Part 2)
        elif action == "UPDATE":
            pid, new_amount = args[0], int(args[1])
            if pid not in payments:
                continue
            if payments[pid]["status"] != REQUIRE_ACTION:
                continue
            if new_amount < 0:
                continue
            payments[pid]["amount"] = new_amount

        # REFUND: pid (Part 3 & 4)
        elif action == "REFUND":
            pid = args[0]
            if pid not in payments:
                continue
            if payments[pid]["status"] != SUCCEEDED:
                continue

            # Part 4: Check timeout window
            if has_time:
                mid = payments[pid]["mid"]
                timeout = merchants[mid]["timeout"]
                succeed_time = payments[pid]["succeed_time"]
                # If timeout is set (not None), check if we're past the window
                if timeout is not None:
                    if succeed_time + timeout < time:
                        continue  # Too late to refund

            payments[pid]["status"] = REFUNDED

    # Calculate final balances
    result = []
    for mid in sorted(merchants.keys()):
        balance = merchants[mid]["balance"]
        for pid in merchants[mid]["payments"]:
            if payments[pid]["status"] == SUCCEEDED:
                balance += payments[pid]["amount"]
        result.append(f"{mid} {balance}")

    return result


# Test runner
if __name__ == "__main__":
    from inputs1 import commands as c1, part as p1
    from inputs2 import commands as c2, part as p2
    from inputs3 import commands as c3, part as p3
    from inputs4 import commands as c4, part as p4

    tests = [
        ("Part 1", c1, p1, ["m1 50", "m2 10"]),
        ("Part 2", c2, p2, ["m1 100"]),
        ("Part 3", c3, p3, ["m1 50"]),
        ("Part 4", c4, p4, ["m1 50"]),
    ]

    for name, cmds, part, expected in tests:
        result = execute(cmds, part)
        status = "✓" if result == expected else "✗"
        print(f"{status} {name}: {result}")
        if result != expected:
            print(f"  Expected: {expected}")
