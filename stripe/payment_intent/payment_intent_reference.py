"""
Reference solution - written as if solving in 60 min timed test.

Strategy:
- Part 1 (~10 min): Get basic INIT/CREATE/ATTEMPT/SUCCEED working
- Part 2 (~5 min): Add UPDATE - quick, just one more case
- Part 3 (~10 min): Add FAIL and REFUND
- Part 4 (~15 min): Add timestamps and timeout logic
- Buffer (~20 min): Debug, edge cases, testing

Key insight: Use multiple simple dicts, not nested dicts with string keys.
"""

from typing import List
from collections import defaultdict

# Status constants
REQUIRE_ACTION = 0
PROCESSING = 1
SUCCEEDED = 2
REFUNDED = 3


def execute(commands: List[str], part: int) -> List[str]:
    # Merchant data - parallel dicts
    m_balance = {}      # mid -> balance
    m_payments = defaultdict(list)  # mid -> [pids]
    m_timeout = {}      # mid -> timeout (None = unlimited)

    # Payment data - parallel dicts
    p_mid = {}          # pid -> merchant id
    p_amount = {}       # pid -> amount
    p_status = {}       # pid -> status constant
    p_succeed_time = {} # pid -> time when succeeded

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
            if timeout is not None and timeout < 0:
                timeout = None
            m_balance[mid] = balance
            m_timeout[mid] = timeout

        # CREATE: pid, mid, amount
        elif action == "CREATE":
            pid, mid, amount = args[0], args[1], int(args[2])
            if mid not in m_balance:
                continue
            if pid in p_mid:
                continue
            if amount <= 0:
                continue
            p_mid[pid] = mid
            p_amount[pid] = amount
            p_status[pid] = REQUIRE_ACTION
            m_payments[mid].append(pid)

        # ATTEMPT: pid
        elif action == "ATTEMPT":
            pid = args[0]
            if pid not in p_mid:
                continue
            if p_status[pid] != REQUIRE_ACTION:
                continue
            p_status[pid] = PROCESSING

        # SUCCEED: pid
        elif action == "SUCCEED":
            pid = args[0]
            if pid not in p_mid:
                continue
            if p_status[pid] != PROCESSING:
                continue
            p_status[pid] = SUCCEEDED
            p_succeed_time[pid] = time

        # FAIL: pid (Part 3)
        elif action == "FAIL":
            pid = args[0]
            if pid not in p_mid:
                continue
            if p_status[pid] != PROCESSING:
                continue
            p_status[pid] = REQUIRE_ACTION

        # UPDATE: pid, new_amount (Part 2)
        elif action == "UPDATE":
            pid, new_amount = args[0], int(args[1])
            if pid not in p_mid:
                continue
            if p_status[pid] != REQUIRE_ACTION:
                continue
            if new_amount < 0:
                continue
            p_amount[pid] = new_amount

        # REFUND: pid (Part 3 & 4)
        elif action == "REFUND":
            pid = args[0]
            if pid not in p_mid:
                continue
            if p_status[pid] != SUCCEEDED:
                continue

            # Part 4: Check timeout window
            if has_time:
                mid = p_mid[pid]
                timeout = m_timeout[mid]
                if timeout is not None:
                    if p_succeed_time[pid] + timeout < time:
                        continue

            p_status[pid] = REFUNDED

    # Calculate final balances
    result = []
    for mid in sorted(m_balance.keys()):
        balance = m_balance[mid]
        for pid in m_payments[mid]:
            if p_status[pid] == SUCCEEDED:
                balance += p_amount[pid]
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
