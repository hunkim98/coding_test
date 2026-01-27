# Bit Font Renderer

## Problem Description

You are building a text rendering system that uses bitmap fonts. A bitmap font stores each character as a grid of pixels, where each pixel is either "on" (filled) or "off" (empty).

Complete the following three functions:

---

## Part 1: Render Character

### Function Signature

```python
def render_character(grid: List[str]) -> List[str]:
```

### Description

Convert a binary character grid into a visual representation:
- `0` becomes `.` (empty pixel)
- `1` becomes `#` (filled pixel)

### Input Format

- `grid`: A list of strings, each containing only `0` and `1` characters

### Output Format

- Return a list of strings with the same dimensions
- Each `0` replaced with `.`
- Each `1` replaced with `#`

### Sample Input

```python
grid = [
    "0000000",
    "0001000",
    "0001000",
    "0101000",
    "0010000"
]
```

### Sample Output

```python
[
    ".......",
    "...#...",
    "...#...",
    ".#.#...",
    "..#...."
]
```

### Constraints

- 1 ≤ len(grid) ≤ 100
- 1 ≤ len(grid[i]) ≤ 100
- Grid contains only characters `0` and `1`

---

## Part 2: Render Word

### Function Signature

```python
def render_word(text: str, font: Dict) -> List[str]:
```

### Description

Render a complete word by joining character grids side-by-side. All characters in a font have the same height but may have different widths.

### Input Format

- `text`: A string of characters to render
- `font`: A dictionary with structure:
  ```python
  {
      "face": "Font Name",
      "chars": {
          "A": ["grid", "rows", ...],
          "B": ["grid", "rows", ...],
          ...
      }
  }
  ```

### Output Format

- Return the rendered word as a list of strings
- Characters are placed directly next to each other (no spacing)
- If text is empty, return an empty list

### Sample Input

```python
font = {
    "face": "Simple Font",
    "chars": {
        "H": [
            "10001",
            "10001",
            "11111",
            "10001",
            "10001"
        ],
        "I": [
            "111",
            "010",
            "010",
            "010",
            "111"
        ]
    }
}

text = "HI"
```

### Sample Output

```python
[
    "#...####",
    "#...#.#.",
    "#####.#.",
    "#...#.#.",
    "#...####"
]
```

### Explanation

The "H" (width 5) and "I" (width 3) are joined horizontally:

```
H       I
#...#   ###
#...#   .#.
#####   .#.
#...#   .#.
#...#   ###
```

Combined and rendered:
```
#...####
#...#.#.
#####.#.
#...#.#.
#...####
```

### Constraints

- 0 ≤ len(text) ≤ 100
- All characters in text exist in the font
- All characters in a font have the same height

---

## Part 3: Render RLE-Encoded Font

### Function Signature

```python
def decode_rle(encoded_rows: List[str]) -> List[str]:

def render_word_rle(text: str, font: Dict) -> List[str]:
```

### Description

Some fonts use Run-Length Encoding (RLE) to compress character data. Decode the RLE data, then render as in Part 2.

#### RLE Encoding Rules

- Each row is encoded as a string of run lengths
- Runs alternate between "off" (0) and "on" (1) pixels
- **Always starts with "off" (0)**
- Digits `0-9` represent lengths 0-9
- Letters `a-z` represent lengths 10-35 (a=10, b=11, ..., z=35)

### Input Format

- `encoded_rows`: List of RLE-encoded strings
- `font`: Same structure as Part 2, but with `"encoding": "rle"` and RLE-encoded character grids

### Output Format

- `decode_rle`: Return decoded binary strings (0s and 1s)
- `render_word_rle`: Return rendered word (same as Part 2)

### Sample Input (decode_rle)

```python
encoded_rows = [
    "532",   # 5 off, 3 on, 2 off
    "343",   # 3 off, 4 on, 3 off
    "a0",    # 10 off, 0 on
    "19"     # 1 off, 9 on
]
```

### Sample Output (decode_rle)

```python
[
    "0000011100",
    "0001111000",
    "0000000000",
    "0111111111"
]
```

### Explanation

```
Encoded: "532"
- 5 off: 00000
- 3 on:  111
- 2 off: 00
Result:  0000011100

Encoded: "a0"
- 10 off: 0000000000
- 0 on:   (nothing)
Result:   0000000000

Encoded: "19"
- 1 off: 0
- 9 on:  111111111
Result:  0111111111
```

### Sample Input (render_word_rle)

```python
rle_font = {
    "face": "Compressed Font",
    "encoding": "rle",
    "chars": {
        "A": [
            "212",    # ..#..
            "11111",  # .#.#.
            "05",     # #####
            "0131",   # #...#
            "0131"    # #...#
        ]
    }
}

text = "A"
```

### Sample Output (render_word_rle)

```python
[
    "..#..",
    ".#.#.",
    "#####",
    "#...#",
    "#...#"
]
```

### Constraints

- Encoded characters use only digits `0-9` and lowercase letters `a-z`
- All decoded rows within a character have the same width
- All characters in the font have the same height

---

## Notes

- Part 2 builds on Part 1 (use `render_character` after combining grids)
- Part 3 builds on Part 2 (decode RLE first, then use Part 2 logic)
- Process characters left-to-right when building words
- The binary grid combination happens before the visual rendering
