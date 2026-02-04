"""
Load Balancer - Reference solution.

Key data structures:
- conn_to_target: dict[str, int]  - which target a connection is on
- target_conns: dict[int, list]   - ordered list of connIds per target
- target_online: dict[int, bool]  - is target online
- next_target: int                - round-robin pointer (1-indexed)
"""
from typing import List


def process_requests(
    num_targets: int,
    max_connections_per_target: int,
    requests: List[str],
) -> List[str]:
    conn_to_target = {}          # connId -> targetId
    target_conns = {}            # targetId -> [connId, ...] in assignment order
    target_online = {}           # targetId -> bool

    for t in range(1, num_targets + 1):
        target_conns[t] = []
        target_online[t] = True

    next_target = 1
    log = []

    def find_target():
        """Find next available target using round-robin. Returns targetId or None."""
        nonlocal next_target
        for _ in range(num_targets):
            t = next_target
            next_target = (next_target % num_targets) + 1
            if target_online[t] and len(target_conns[t]) < max_connections_per_target:
                return t
        return None

    def assign(conn_id):
        """Try to assign a connection. Returns True if successful."""
        t = find_target()
        if t is None:
            return False
        conn_to_target[conn_id] = t
        target_conns[t].append(conn_id)
        log.append(f"({conn_id}, {t})")
        return True

    for req in requests:
        parts = req.split(" ")
        cmd = parts[0]

        if cmd == "CONNECT":
            conn_id = parts[1]
            if conn_id in conn_to_target:
                # Duplicate: log original assignment, don't change state
                log.append(f"({conn_id}, {conn_to_target[conn_id]})")
            else:
                assign(conn_id)

        elif cmd == "DISCONNECT":
            conn_id = parts[1]
            if conn_id in conn_to_target:
                t = conn_to_target[conn_id]
                target_conns[t].remove(conn_id)
                del conn_to_target[conn_id]

        elif cmd == "SHUTDOWN":
            target_id = int(parts[1])
            target_online[target_id] = False
            # Evict connections in assignment order
            evicted = list(target_conns[target_id])
            target_conns[target_id] = []
            for conn_id in evicted:
                del conn_to_target[conn_id]
            # Try to reassign each evicted connection
            for conn_id in evicted:
                assign(conn_id)

    return log


# Test runner
if __name__ == "__main__":
    from inputs1 import test_cases as t1, part as p1
    from inputs2 import test_cases as t2, part as p2
    from inputs3 import test_cases as t3, part as p3
    from inputs4 import test_cases as t4, part as p4
    from inputs5 import test_cases as t5, part as p5

    all_tests = [(p1, t1), (p2, t2), (p3, t3), (p4, t4), (p5, t5)]

    for part_num, tests in all_tests:
        print(f"Part {part_num}:")
        for i, tc in enumerate(tests):
            result = process_requests(tc["num_targets"], tc["max_conns"], tc["requests"])
            passed = result == tc["expected"]
            status = "PASS" if passed else "FAIL"
            print(f"  {status}: Test {i + 1}")
            if not passed:
                print(f"    Expected: {tc['expected']}")
                print(f"    Got:      {result}")
    print("\nDone!")
