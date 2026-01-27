"""
HTTP Request Language Matching

Part 1: Exact matches only
Part 2: Prefix matching (en -> en-US, en-GB)
Part 3: Wildcards (*)
Part 4: Quality scores (q=0.8)
"""

from typing import List, Tuple

# Change this import to test different parts
from inputs1 import test_cases, part
# from inputs2 import test_cases, part
# from inputs3 import test_cases, part
# from inputs4 import test_cases, part


def parse_accept_language(accept_header: str, supported_languages: List[str]) -> List[str]:
    """
    Parse Accept-Language header and return matching supported languages.

    Args:
        accept_header: Comma-separated language preferences
        supported_languages: List of languages the server supports

    Returns:
        List of matching languages in preference order
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def parse_language_with_q(entry: str) -> Tuple[str, float]:
    """
    Part 4 helper: Extract language and q-value from entry.

    Args:
        entry: Language entry like "en-US" or "fr-FR;q=0.8"

    Returns:
        Tuple of (language, q_value)
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def is_prefix_match(generic: str, specific: str) -> bool:
    """
    Part 2 helper: Check if generic code matches specific language.

    Args:
        generic: Generic code like "en"
        specific: Specific code like "en-US"

    Returns:
        True if generic matches specific
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Test runner
def run_tests():
    print(f"Testing Part {part}")
    print("=" * 60)

    all_passed = True
    for i, tc in enumerate(test_cases):
        result = parse_accept_language(tc["accept_header"], tc["supported"])
        expected = tc["expected"]
        passed = result == expected

        status = "✓" if passed else "✗"
        print(f"{status} Test {i + 1}")
        print(f"   Header:    {tc['accept_header']}")
        print(f"   Supported: {tc['supported']}")
        print(f"   Expected:  {expected}")
        print(f"   Got:       {result}")
        print()

        if not passed:
            all_passed = False

    return all_passed


if __name__ == "__main__":
    run_tests()
