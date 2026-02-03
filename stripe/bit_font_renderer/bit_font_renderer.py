"""
Bit Font Renderer

Part 1: Render a single character (0 -> '.', 1 -> '#')
Part 2: Render a word by joining characters horizontally
Part 3: Decode RLE-encoded fonts and render
"""

from typing import List, Dict

# Change this import to test different parts
from inputs1 import *

from inputs2 import *

from inputs3 import *


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
    result = []
    for row in grid:
        r_row = []
        for col in row:
            if col == "0":
                r_row.append(".")
            elif col == "1":
                r_row.append("#")
            else:
                raise Exception("Unrecognized char")
        result.append(r_row)

    return result


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
    # let us look through the tallest and we will prepend
    tallest_row = 0
    for fkey in font["chars"]:
        char = font["chars"][fkey]
        char_h = len(char)
        if char_h > tallest_row:
            tallest_row = char_h

    unified_font: Dict = {}
    for fkey in font["chars"].keys():
        char = font["chars"][fkey]
        char_h = len(char)
        new_char = font["chars"][fkey]
        if char_h < tallest_row:
            new_char = ([] * (tallest_row - char_h)).extend(font["chars"][fkey])
        unified_font[fkey] = new_char

    result = []
    for i in range(tallest_row):
        r_row = []
        for fkey in text:
            char = unified_font[fkey]
            char_row = char[i]
            for col in char_row:
                if col == "0":
                    r_row.append(".")
                elif col == "1":
                    r_row.append("#")
                else:
                    raise Exception("Unrecognized char")
        result.append(r_row)
    return result


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
    decoded = []
    for row in encoded_rows:
        is_zero = True
        d_row = ""
        # print(row, "start")
        for col in row:
            occ = None
            if col == "0":
                occ = 0
            elif not col.isdigit():
                occ = ord(col) + 10
                occ -= ord("a")
            else:
                occ = int(col)

            if occ != 0:
                if is_zero:
                    d_row += "0" * occ
                else:
                    d_row += "1" * occ
            is_zero = not is_zero
        # print(d_row, "0" * 0)
        decoded.append(d_row)
    max_width = max(len(row) for row in decoded)
    result = []
    for row in decoded:
        new_row = row
        if len(row) != max_width:
            new_row += "0" * (max_width - len(row))
        result.append(new_row)

    return result


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
    decoded_font = {}
    for fkey in font["chars"]:
        char = font["chars"][fkey]
        decoded = decode_rle(char)
        decoded_font[fkey] = decoded

    font["chars"] = decoded_font
    return render_word(text, font)


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
