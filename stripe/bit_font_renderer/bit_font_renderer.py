"""
Bit Font Renderer

Part 1: Render a single character (0 -> '.', 1 -> '#')
Part 2: Render a word by joining characters horizontally
Part 3: Decode RLE-encoded fonts and render
"""

from typing import List, Dict

# Change this import to test different parts
from inputs1 import *
# from inputs2 import *
# from inputs3 import *


def render_character(grid: List[str]) -> List[str]:
    """
    Part 1: Convert binary grid to visual representation.

    Args:
        grid: List of strings containing '0' and '1'

    Returns:
        List of strings with '0' -> '.' and '1' -> '#'
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def render_word(text: str, font: Dict) -> List[str]:
    """
    Part 2: Render a word using the given font.

    Args:
        text: String to render
        font: Font dictionary with 'chars' mapping

    Returns:
        List of strings representing the rendered word
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def decode_rle(encoded_rows: List[str]) -> List[str]:
    """
    Part 3a: Decode RLE-encoded rows.

    RLE rules:
    - Alternates between off (0) and on (1), starting with off
    - Digits 0-9 = lengths 0-9
    - Letters a-z = lengths 10-35

    Args:
        encoded_rows: List of RLE-encoded strings

    Returns:
        List of decoded binary strings
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def render_word_rle(text: str, font: Dict) -> List[str]:
    """
    Part 3b: Render a word using an RLE-encoded font.

    Args:
        text: String to render
        font: RLE-encoded font dictionary

    Returns:
        List of strings representing the rendered word
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Test runner
if __name__ == "__main__":
    if part == 1:
        result = render_character(grid)
        print("Rendered character:")
        for row in result:
            print(row)

    elif part == 2:
        result = render_word(text, font)
        print(f"Rendered '{text}':")
        for row in result:
            print(row)

    elif part == 3:
        # Test decode_rle
        print("Decoded RLE:")
        decoded = decode_rle(encoded_rows)
        for row in decoded:
            print(row)

        print(f"\nRendered '{rle_text}' from RLE font:")
        result = render_word_rle(rle_text, rle_font)
        for row in result:
            print(row)
