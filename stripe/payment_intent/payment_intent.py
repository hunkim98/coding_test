from typing import List

# Change this import to test different parts
from inputs1 import commands, part

# Expected outputs:
# Part 1 (inputs1): m1 50, m2 10
# Part 2 (inputs2): m1 100
# Part 3 (inputs3): m1 50
# Part 4 (inputs4): m1 50


def execute(commands: List[str], part: int) -> List[str]:
    """
    Execute a list of commands to manage Payment Intents and return merchant balances.

    Args:
        commands: List of command strings
        part: Which part of the problem (1, 2, 3, or 4)

    Returns:
        List of merchant balances sorted alphabetically, e.g., ['m1 50', 'm2 100']

    Commands by part:
        Part 1: INIT, CREATE, ATTEMPT, SUCCEED
        Part 2: Part 1 + UPDATE
        Part 3: Part 2 + FAIL, REFUND
        Part 4: Part 3 + Timestamps + refund_timeout_limit

    States: REQUIRES_ACTION -> PROCESSING -> COMPLETED
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Run and print result
result = execute(commands, part)
if result:
    print("\n".join(result))
