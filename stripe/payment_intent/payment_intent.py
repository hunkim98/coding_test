from collections import defaultdict
from typing import List

# Change this import to test different parts
from inputs4 import commands, part

# Expected outputs:
# Part 1 (inputs1): m1 50, m2 10
# Part 2 (inputs2): m1 100
# Part 3 (inputs3): m1 50
# Part 4 (inputs4): m1 50


def parse_time_cmd(
    cmd: str,
    mbal: dict[int],
    mpid: dict[list[str]],
    pamt: dict[int],
    pstat: dict[int],
    ptom: dict[str],
    mtout: dict[int],
    ptime: dict,
):
    cmd_type = cmd.split(" ")[1].strip()
    if cmd_type == "INIT":
        if len(cmd.split(" ")) > 4:
            t, _, mid, start_bal, tout = cmd.split(" ")
        else:
            t, _, mid, start_bal = cmd.split(" ")
            tout = None
        mbal[mid] = int(start_bal)
        mpid[mid] = []
        if tout is not None:
            tout = int(tout)
            if tout < 0:
                mtout[mid] = None
            elif tout == 0:
                mtout[mid] = 0
            else:
                mtout[mid] = tout
    elif cmd_type == "CREATE":
        t, _, pid, mid, amt = cmd.split(" ")
        if mid not in mpid:
            return
        if pstat.get(pid) is not None:
            return
        if int(amt) <= 0:
            return
        mpid[mid].append(pid)
        pamt[pid] = int(amt)  # we store the amount
        pstat[pid] = 0  # REQUIRE ACTION
        ptom[pid] = mid
    elif cmd_type == "ATTEMPT":
        t, _, pid = cmd.split(" ")
        if pstat.get(pid) is None:
            return
        if pstat[pid] != 0:
            return
        pstat[pid] = 1  # PROCESSING
    elif cmd_type == "SUCCEED":
        t, _, pid = cmd.split(" ")
        if pstat.get(pid) is None:
            return
        if pstat[pid] != 1:
            return
        pstat[pid] = 2
        ptime[pid] = int(t)
    elif cmd_type == "UPDATE":
        t, _, pid, namt = cmd.split(" ")
        if int(namt) < 0:
            return
        if pstat.get(pid) != 0:
            return
        pamt[pid] = int(namt)
    elif cmd_type == "FAIL":
        t, _, pid = cmd.split(" ")
        if pstat.get(pid) != 1:
            return
        pstat[pid] = 0
    elif cmd_type == "REFUND":
        t, _, pid = cmd.split(" ")
        if pstat.get(pid) != 2:
            return
        if pstat.get(pid) == 3:
            return
        mid = ptom[pid]
        if mtout.get(mid) is not None:
            tout = mtout[mid]
            succeed_t = ptime[pid]
            if tout + succeed_t < int(t):
                return
        pstat[pid] = 3
        pamt[pid] = 0
        pass
    else:
        raise Exception("Unrecognized cmd type")


def parse_cmd(
    cmd: str,
    mbal: dict[int],
    mpid: dict[list[str]],
    pamt: dict[int],
    pstat: dict[int],
):
    # INIT
    # CREATE
    # ATTEMPT
    cmd_type = cmd.split(" ")[0].strip()

    if cmd_type == "INIT":
        _, mid, start_bal = cmd.split(" ")
        mbal[mid] = int(start_bal)
        mpid[mid] = []
    elif cmd_type == "CREATE":
        _, pid, mid, amt = cmd.split(" ")
        if mid not in mpid:
            return
        if pstat.get(pid) is not None:
            return
        if int(amt) <= 0:
            return
        mpid[mid].append(pid)
        pamt[pid] = int(amt)  # we store the amount
        pstat[pid] = 0  # REQUIRE ACTION
    elif cmd_type == "ATTEMPT":
        _, pid = cmd.split(" ")
        if pstat.get(pid) is None:
            return
        if pstat[pid] != 0:
            return
        pstat[pid] = 1  # PROCESSING
    elif cmd_type == "SUCCEED":
        _, pid = cmd.split(" ")
        if pstat.get(pid) is None:
            return
        if pstat[pid] != 1:
            return
        pstat[pid] = 2
    elif cmd_type == "UPDATE":
        _, pid, namt = cmd.split(" ")
        if int(namt) < 0:
            return
        if pstat.get(pid) != 0:
            return
        pamt[pid] = int(namt)
    elif cmd_type == "FAIL":
        _, pid = cmd.split(" ")
        if pstat.get(pid) != 1:
            return
        pstat[pid] = 0
    elif cmd_type == "REFUND":
        _, pid = cmd.split(" ")
        if pstat.get(pid) != 2:
            return
        if pstat.get(pid) == 3:
            return
        pstat[pid] = 3
        pamt[pid] = 0
        pass
    else:
        raise Exception("Unrecognized cmd type")


def execute(commands: List[str], part: int) -> List[str]:
    # -----------------------------
    # Your implementation here
    # -----------------------------
    # return the account balances for each merchant after all executions
    # type: list of strings (item: "{mch} {balance}")
    # sort by merchant id in ascending
    mbal = defaultdict()
    mpid = defaultdict(list)
    pamt = defaultdict(int)
    pstat = defaultdict()
    ptom = defaultdict()
    mtout = defaultdict()
    ptime = defaultdict()

    init_cmd = commands[0]
    cmd_type = init_cmd.split(" ")[0].strip()

    has_time = False
    try:
        _ = int(cmd_type)
        has_time = True
    except:
        has_time = False

    for cmd in commands:
        if has_time:
            parse_time_cmd(
                cmd=cmd,
                mbal=mbal,
                mpid=mpid,
                pamt=pamt,
                pstat=pstat,
                ptom=ptom,
                mtout=mtout,
                ptime=ptime,
            )
        else:
            parse_cmd(cmd=cmd, mbal=mbal, mpid=mpid, pamt=pamt, pstat=pstat)

    for key in sorted(mpid.keys()):
        pids = mpid.get(key)
        for id in pids:
            if pstat.get(id) == 2:
                mbal[key] += pamt[id]
        print(f"{key} {mbal[key]}")


# Run and print result
result = execute(commands, part)
if result:
    print("\n".join(result))
