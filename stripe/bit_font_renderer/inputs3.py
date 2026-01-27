# Part 3: RLE Decoding and Rendering
#
# decode_rle expected output:
# [
#     "0000011100",
#     "0001111000",
#     "0000000000",
#     "0111111111"
# ]
#
# render_word_rle("A") expected output:
# [
#     "..#..",
#     ".#.#.",
#     "#####",
#     "#...#",
#     "#...#"
# ]

part = 3

# Test data for decode_rle
encoded_rows = [
    "532",   # 5 off, 3 on, 2 off  -> "0000011100"
    "343",   # 3 off, 4 on, 3 off  -> "0001111000"
    "a0",    # 10 off, 0 on        -> "0000000000"
    "19"     # 1 off, 9 on         -> "0111111111"
]

# RLE-encoded font
rle_font = {
    "face": "Compressed Font",
    "encoding": "rle",
    "chars": {
        "A": [
            "212",    # ..#..  (2 off, 1 on, 2 off)
            "11111",  # .#.#.  (1 off, 1 on, 1 off, 1 on, 1 off)
            "05",     # #####  (0 off, 5 on)
            "0131",   # #...#  (0 off, 1 on, 3 off, 1 on)
            "0131"    # #...#
        ],
        "B": [
            "041",    # ####.  (0 off, 4 on, 1 off)
            "01211",  # #..#.  (0 off, 1 on, 2 off, 1 on, 1 off)
            "0311",   # ###..  (0 off, 3 on, 1 off, 1 off... wait)
            "01211",  # #..#.
            "041"     # ####.
        ],
        "C": [
            "14",     # .####
            "01",     # #....  (but need 5 wide)
            "01",     # #....
            "01",     # #....
            "14"      # .####
        ]
    }
}

rle_text = "A"
