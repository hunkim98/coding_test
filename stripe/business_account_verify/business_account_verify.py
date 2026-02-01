"""
Business Account Verification

Part 1: Check for missing fields
Part 2: Validate description length (5-31 chars)
Part 3: Block generic names (ONLINE STORE, ECOMMERCE, etc.)
Part 4: Match business names (50% word overlap)
Part 5: Return specific error codes
"""

from collections import defaultdict
from typing import List, Set

# Change this import to test different parts
# from inputs1 import csv_data, part

# from inputs2 import csv_data, part

# from inputs3 import csv_data, part

from inputs4 import csv_data, part

# from inputs5 import csv_data, part, is_input5

BLOCKED_DESC = [
    "ONLINE STORE",
    "ECOMMERCE",
    "RETAIL",
    "SHOP",
    "GENERAL MERCHANDISE",
]


def check_empty(args) -> bool:
    is_valid = True
    for a in args:
        if not a:
            is_valid = False
            break
    return is_valid


def check_desc_len(args) -> bool:
    desc = args[4].strip()
    if len(desc) >= 5 and len(desc) <= 31:
        return True
    else:
        return False


def check_desc_gen(args) -> bool:
    desc = args[4].strip()
    if desc.upper() in BLOCKED_DESC:
        return False
    else:
        return True


def prune_char(text: str):
    pruned = text
    if " llc" in text.lower():
        start_i = text.lower().index(" llc")
        end_i = start_i + 4
        pruned = text[0:start_i] + text[end_i:]
    if " inc" in pruned.lower():
        start_i = pruned.lower().index(" inc")
        end_i = start_i + 4
        pruned = pruned[0:start_i] + pruned[end_i:]
    return pruned


def check_name(args) -> bool:
    name = args[1] if args[1] is not None else ""
    if name is None:
        return False
    # remove LLC or Inc in name and desc
    short_desc = args[3]
    full_desc = args[4]
    p_name = prune_char(name)
    p_short_desc = prune_char(short_desc)
    p_full_desc = prune_char(full_desc)
    name_words = p_name.split(" ")

    valid_cnt = 0
    for word in name_words:
        try:
            p_short_desc.lower().index(word.lower())
            valid_cnt += 1
        except:
            pass
    if valid_cnt / len(name_words) >= 0.5:
        return True

    valid_cnt = 0
    for word in name_words:
        try:
            p_full_desc.lower().index(word.lower())
            valid_cnt += 1
        except:
            pass

    if valid_cnt / len(name_words) >= 0.5:
        return True
    return False


def check_err(args) -> bool:
    pass


def validate_businesses(csv_data: str) -> str:
    """
    Validate business accounts from CSV data.

    Args:
        csv_data: CSV string with header row and business data

    Returns:
        String with one line per business showing validation result
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    # ignore
    # col1: Business ID
    # col2: Legal Name (used in output)
    # col3: Website URL
    # col4: Short Description
    # col5: Full Description (main validation target)
    # col6: Product Details
    b_status = defaultdict(lambda: False)
    csv_rows = csv_data.split("\n")
    for row in csv_rows[1:]:
        args = row.split(",")
        name = args[1] if args[1] is not None else ""
        b_status[name] = check_empty(args)
        if b_status[name] is True:
            b_status[name] = check_desc_len(args)
        if b_status[name] is True:
            b_status[name] = check_desc_gen(args)
        if b_status[name] is True:
            b_status[name] = check_name(args)

    for b in b_status:
        if b_status[b] is True:
            print(f"VERIFIED: {b}")
        else:
            print(f"NOT VERIFIED: {b}")


def validate_businesses2(csv_data: str) -> str:
    """
    Validate business accounts from CSV data.

    Args:
        csv_data: CSV string with header row and business data

    Returns:
        String with one line per business showing validation result
    "ERROR_MISSING_FIELDS"
    "ERROR_INVALID_LENGTH"
    "ERROR_GENERIC_NAME"
    "ERROR_NAME_MISMATCH"
    """
    b_status = defaultdict(lambda: "VERIFIED")
    csv_rows = csv_data.split("\n")
    for row in csv_rows[1:]:
        args = row.split(",")
        name = args[1] if args[1] is not None else ""
        if not check_empty(args):
            b_status[name] = "ERROR_MISSING_FIELDS"
        if not check_desc_len(args) and b_status[name] == "VERIFIED":
            b_status[name] = "ERROR_INVALID_LENGTH"
        if not check_desc_gen(args) and b_status[name] == "VERIFIED":
            b_status[name] = "ERROR_GENERIC_NAME"
        if not check_name(args) and b_status[name] == "VERIFIED":
            b_status[name] = "ERROR_NAME_MISMATCH"

    for b in b_status:
        print(f"{b_status[b]}: {b}")


# Test runner
if __name__ == "__main__":
    try:
        if is_input5 is not None:
            pass
        result = validate_businesses2(csv_data)
    except:
        result = validate_businesses(csv_data)
