"""
Business Account Verification

Part 1: Check for missing fields
Part 2: Validate description length (5-31 chars)
Part 3: Block generic names (ONLINE STORE, ECOMMERCE, etc.)
Part 4: Match business names (50% word overlap)
Part 5: Return specific error codes
"""

from typing import List, Set

# Change this import to test different parts
from inputs1 import csv_data, part
# from inputs2 import csv_data, part
# from inputs3 import csv_data, part
# from inputs4 import csv_data, part
# from inputs5 import csv_data, part

# Blocked terms for Part 3
BLOCKED_TERMS = {
    'ONLINE STORE',
    'ECOMMERCE',
    'RETAIL',
    'SHOP',
    'GENERAL MERCHANDISE'
}

# Words to ignore when matching names (Part 4)
IGNORED_WORDS = {'llc', 'inc'}


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
    pass


def check_missing_fields(fields: List[str]) -> bool:
    """
    Part 1: Check if all fields are non-empty.

    Args:
        fields: List of 6 field values

    Returns:
        True if all fields have content, False otherwise
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def check_description_length(full_description: str) -> bool:
    """
    Part 2: Check if description length is valid (5-31 chars).

    Args:
        full_description: The col5 value

    Returns:
        True if length is valid, False otherwise
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def check_blocked_terms(full_description: str) -> bool:
    """
    Part 3: Check if description contains blocked terms.

    Args:
        full_description: The col5 value

    Returns:
        True if NO blocked terms found (valid), False otherwise
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def get_words(text: str) -> Set[str]:
    """
    Helper: Extract words from text, removing ignored words.

    Args:
        text: Input string

    Returns:
        Set of lowercase words (excluding LLC, Inc)
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def check_name_match(business_name: str, short_desc: str, full_desc: str) -> bool:
    """
    Part 4: Check if at least 50% of business name words match descriptions.

    Args:
        business_name: The col2 value
        short_desc: The col4 value
        full_desc: The col5 value

    Returns:
        True if >= 50% match, False otherwise
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Test runner
if __name__ == "__main__":
    result = validate_businesses(csv_data)
    print(result)
