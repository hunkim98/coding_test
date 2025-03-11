from typing import List


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    result = []
    cur_width = 0
    cur_start = 0
    cur_end = 0
    lines = []
    cur_line = []
    for i in range(len(words)):
        word = words[i]
        add_width = len(word)
        cur_line.append(word)
        if len(cur_line) > 1:
            add_width += 1  # we need to add space

        if cur_width + add_width > maxWidth:
            cur_end = i
            lines.append(words[cur_start:cur_end])
            cur_start = i
            cur_line = [words[cur_start]]  # start with new
            cur_width = len(words[cur_start])  # reset
        else:
            cur_width += add_width

    if cur_end < len(words):
        lines.append(words[cur_start:])

    # print(lines)
    for line_idx in range(len(lines)):
        line_words = lines[line_idx]
        use_space = 0
        for word in line_words:
            use_space += len(word)
        left_space = maxWidth - use_space
        final_line = ""
        for i in range(maxWidth):
            final_line += " "
        final_line = list(final_line)
        if line_idx == len(lines) - 1:
            cur_i = 0
            for j in range(len(line_words)):
                word = line_words[j]
                for k in range(len(word)):
                    final_line[cur_i + k] = word[k]
                cur_i += len(word) + 1
        else:
            if len(line_words) == 1:
                for j in range(len(line_words[0])):
                    final_line[j] = line_words[0][j]
            elif len(line_words) == 2:
                for j in range(len(line_words[0])):
                    final_line[j] = line_words[0][j]
                for j in range(len(line_words[1])):
                    k = maxWidth - len(line_words[1]) + j
                    final_line[k] = line_words[1][j]
            else:
                # for j in range(len(line_words[0])):
                #     final_line[j] = line_words[0][j]
                # for j in range(len(line_words[-1])):
                #     k = maxWidth - len(line_words[-1]) + j
                #     final_line[k] = line_words[-1][j]

                min_space = left_space // (len(line_words) - 1)
                spaces = []
                spaces.append(0)
                for k in range(len(line_words) - 1):
                    spaces.append(min_space)
                residual = left_space - min_space * (len(line_words) - 1)

                for k in range(len(spaces)):
                    if residual > 0:
                        spaces[k + 1] += 1
                        residual -= 1

                cur_i = 0
                for k in range(len(line_words)):
                    word = line_words[k]
                    cur_i += spaces[k]
                    for l in range(cur_i, cur_i + len(word)):
                        final_line[l] = word[l - cur_i]
                    cur_i += len(word)

            # for k in range(1, len(line_words) - 1):
            #     pass

        # print("|" + "".join(final_line) + "|")
        result.append("".join(final_line))

    # print(lines)
    return result


if __name__ == "__main__":
    assert fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    ) == ["This    is    an", "example  of text", "justification.  "]
    assert fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16) == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        ",
    ]
    assert fullJustify(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    ) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
