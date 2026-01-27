Bit Font Renderer Problem

Problem Summary

You need to build a system that draws text using bitmap fonts. A bitmap font saves each character as a grid of pixels. A pixel is either "on" (filled) or "off" (empty).

This problem has three parts:

1. Draw One Character: Change a grid of 0s and 1s into a picture using . and #.
2. Draw a Word: Join multiple characters side-by-side to make a word.
3. Compressed Fonts: specific fonts use a compression method called Run-Length Encoding (RLE). You need to decode them.

Input Data Format

Character Grid: A character is a list of strings. Each string is a row of the grid. It only contains 0 (off) and 1 (on).

```python
# Example: Letter 'J' as a 5x7 grid
letter_j = [
    "0000000",
    "0001000",
    "0001000",
    "0101000",
    "0010000"
]
```

Font Dictionary: This connects a character name to its grid.

```python
font = {
    "face": "Simple Font",
    "chars": {
        "H": ["10001", "10001", "11111", "10001", "10001"],
        "I": ["11111", "00100", "00100", "00100", "11111"],
        # ... more characters
    }
}
```

Part 1: Draw One Character

The Task

Write a function called render_character(grid). It takes a list of strings with 0s and 1s. It returns a new list where:

- 0 becomes . (empty pixel)
- 1 becomes # (filled pixel)

Example

Input:

```python
grid = [
    "0000000",
    "0001000",
    "0001000",
    "0101000",
    "0010000"
]
```

Output:

```python
render_character(grid) == [
    ".......",
    "...#...",
    "...#...",
    ".#.#...",
    "..#...."
]
```

When printed:

```
.......
...#...
...#...
.#.#...
..#....
```

Part 1 Requirements

- The function must work with grids of any size.
- The output must be a list of strings.
- The input will only contain 0 and 1.

Part 2: Draw a Word

The Task

Now, write a function called render_word(text, font). This function takes a string of text and a font. It joins the characters together side-by-side to make a word.

Example

Input:

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

Output:

```python
render_word("HI", font) == [
    "#...####",
    "#...#.#.",
    "#####.#.",
    "#...#.#.",
    "#...####"
]
```

When printed:

```
#...####
#...#.#.
#####.#.
#...#.#.
#...####
```

Part 2 Requirements

- Place characters next to each other. Do not add extra space between them.
- All characters in one font have the same height.
- Characters can have different widths.
- If the text is empty, return an empty list.
- Join the binary strings first, then change them to visual symbols (. and #).

Questions to Ask the Interviewer

- Do we need space between the letters?
- Are the heights always the same for every letter?
- What happens if a letter is missing from the font?
- Do we need to handle newlines?

Part 3: Compressed Fonts (RLE)

The Task

Some fonts use Run-Length Encoding (RLE) to save space. This method stores the count of repeated pixels instead of every single pixel.

Here is how the encoding works:

- Each row is a string of characters. These characters represent lengths.
- The pixels alternate between "off" (0) and "on" (1).
- Always start with "off" (0).
- Digits 0-9 mean a length of 0 to 9.
- Letters a-z mean a length of 10 to 35 (where a is 10, b is 11, etc.).

Write a function called decode_rle(encoded_rows) to turn this compressed data back into full strings of 0s and 1s.

Example

How Decoding Works:

```
Original row: "0000011100"  (5 zeros, 3 ones, 2 zeros)
Encoded:      "532"         (5 off, 3 on, 2 off)
```

Input:

```python
encoded_char = [
    "532",      # 5 off, 3 on, 2 off  -> "0000011100"
    "343",      # 3 off, 4 on, 3 off  -> "0001111000"
    "a0",       # 10 off, 0 on        -> "0000000000"
    "19"        # 1 off, 9 on         -> "0111111111"
]
```

After Decoding:

```python
decode_rle(encoded_char) == [
    "0000011100",
    "0001111000",
    "0000000000",
    "0111111111"
]
```

After Rendering (using Part 1 logic):

```
.....###..
...####...
..........
.#########
```

Part 3 Requirements

- Rows always start with "off" (0) pixels.
- The pattern switches back and forth: off -> on -> off -> on.
- 0-9 represent numbers 0-9.
- a-z represent numbers 10-35.
- All rows must end up being the same width.
- After decoding, render the grid just like in Part 1.

Final Function

Write render_word_rle(text, font) to handle these compressed fonts:

```python
rle_font = {
    "face": "Compressed Font",
    "encoding": "rle",
    "chars": {
        "A": ["212", "11111", "05", "0131", "0131"],
        # "212"   -> ..#.. (2 off, 1 on, 2 off)
        # "11111" -> .#.#. (1 off, 1 on, 1 off, 1 on, 1 off)
        # "05"    -> ##### (0 off, 5 on)
        # "0131"  -> #...# (0 off, 1 on, 3 off, 1 on)
        # ... more characters
    }
}
```

Bonus Question: Multiple Font Types

The interviewer might ask you to support different fonts in one system. Your code should check the font name and decide which function to use.
