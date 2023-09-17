# 세로 크기: N / 가로 크기: M (outer celss are blocked)
# make the red marble escape the board through a  hole
# actions: left tilt, right tilt, up tilt,e bottom tile
# all balls move simultaneously
# each ball cannot be in the same area
# We stop tilting when the marbles do not move any more

# Question: When the marble state is given, what is the least amount of time necessary for taking the red marble out
# The red should only go through the hole
# BFS


import sys

# the first line will contain the number of lines to consider
n, m = map(int, sys.stdin.readline().split())  # first line
# ignore the \n
arr = [sys.stdin.readline().strip() for _ in range(n)]

visitable_lot = {}

# we subtract 2 from each place since we do not care about the outer parts
# visitable = [[True] * (m-2)] * (n-2)
visitable = []


for i in range(n-2):
    temp = []
    for j in range(m-2):
        temp.append(True)
    visitable.append(temp)


curr_r = {
    "r_idx": -1,
    "c_idx": -1
}
curr_b = {
    "r_idx": -1,
    "c_idx": -1
}

hole = {
    "r_idx": -1,
    "c_idx": -1
}

# set the locations
for r_idx, row in enumerate(arr):
    if r_idx == 0 or r_idx == n-1:
        continue

    for c_idx, col in enumerate(row):
        if c_idx == 0 or c_idx == m-1:
            continue
        visit_r_idx = r_idx - 1
        visit_c_idx = c_idx - 1
        if col == "#":
            visitable[visit_r_idx][visit_c_idx] = False
        elif col == ".":
            visitable[visit_r_idx][visit_c_idx] = True
        elif col == "B":
            curr_b["r_idx"] = visit_r_idx
            curr_b["c_idx"] = visit_c_idx
        elif col == "R":
            curr_r["r_idx"] = visit_r_idx
            curr_r["c_idx"] = visit_c_idx
        elif col == "O":
            hole["c_idx"] = visit_c_idx
            hole["r_idx"] = visit_r_idx

# element of [row_change, col_change]
deltas = [[-1, 0], [1, 0], [0, 1], [0, -1]]

# we can either tilt left, top, right, bottom
# we save status for node
queue = [{"r": [curr_r["r_idx"], curr_r["c_idx"]],
          "b": [curr_b["r_idx"], curr_b["c_idx"]], "level": 1}]


turns = -1
visited = [[[[False]*(m-2) for _ in range(n-2)]
            for _ in range(m-2)] for _ in range(n-2)]
while len(queue) != 0:

    element = queue.pop(0)  # this takes the first element
    r_row = element["r"][0]
    r_col = element["r"][1]

    b_row = element["b"][0]
    b_col = element["b"][1]
    visited[r_row][r_col][b_row][b_col] = True

    is_finished = False

    for delta in deltas:
        r_next_row = r_row
        r_next_col = r_col
        b_next_row = b_row
        b_next_col = b_col

        bigger_edge = n
        if m > n:
            bigger_edge = m
        # we have n rows
        # we need to compare r and b together one by one
        is_r_out = False
        is_b_out = False
        for i in range(bigger_edge-2):
            r_next_row = r_next_row
            r_next_col = r_next_col
            b_next_row = b_next_row
            b_next_col = b_next_col

            r_movable = True
            b_movable = True
            if r_next_row + delta[0] >= n - 2 or r_next_row + delta[0] < 0 or r_next_col + delta[1] >= m - 2 or r_next_col + delta[1] < 0:
                # out of bound
                r_movable = False
            else:
                r_movable = visitable[r_next_row +
                                      delta[0]][r_next_col + delta[1]]

            if b_next_row + delta[0] >= n - 2 or b_next_row + delta[0] < 0 or b_next_col + delta[1] >= m - 2 or b_next_col + delta[1] < 0:
                # out of bound
                b_movable = False
            else:
                b_movable = visitable[b_next_row +
                                      delta[0]][b_next_col + delta[1]]

            if r_movable:
                # if not movable we cancel the movement
                r_next_row = r_next_row + delta[0]
                r_next_col = r_next_col + delta[1]

            if b_movable:
                # if not movable we cancel the movement
                b_next_row = b_next_row + delta[0]
                b_next_col = b_next_col + delta[1]

            if r_movable and not b_movable:
                if r_next_row == b_next_row and r_next_col == b_next_col:
                    # cancel r move
                    r_next_row = r_next_row - delta[0]
                    r_next_col = r_next_col - delta[1]
            elif not r_movable and b_movable:
                if r_next_row == b_next_row and r_next_col == b_next_col:
                    # cancel r move
                    b_next_row = b_next_row - delta[0]
                    b_next_col = b_next_col - delta[1]

            if hole["r_idx"] == r_next_row and hole["c_idx"] == r_next_col:
                is_r_out = True

            if hole["r_idx"] == b_next_row and hole["c_idx"] == b_next_col:
                is_b_out = True

            if is_b_out:
                # we do not need to look at this operation since it failed
                break
            if not r_movable and not b_movable:
                # we do not need to change anymore
                # we do not need to continue the operation
                break

        if r_row == r_next_row and r_col == r_next_col and b_row == b_next_row and b_col == b_next_col:
            # nothing changed
            continue

        if is_b_out:
            continue

        # this is when we have finished the tilt operation
        if is_r_out:
            # this means we are successful
            turns = element["level"]
            is_finished = True

        # print(r_next_row, r_next_col, b_next_row, b_next_col)

        elif not is_r_out and not is_b_out and not visited[r_next_row][r_next_col][b_next_row][b_next_col]:
            # continue to find answer
            queue.append({"r": [r_next_row, r_next_col],
                          "b": [b_next_row, b_next_col], "level": element["level"] + 1})

    if is_finished:
        break

print(turns)
# Input Ex 1
# 0은 구멍의 위치
# 10번 이하로 빨ㄴ 구슬을 구멍으로 뺄 수 없으면 -1

#  5 5
#  #####
#  #..B#
#  #.#.#
#  #RO.#
#  #####

# answer: 1
