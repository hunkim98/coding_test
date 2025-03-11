from typing import List
from collections import deque

dx = [1, 0, -1, 0]  # the order is important
# right, bottom, left, up
dy = [0, 1, 0, -1]


def makeId(x, y):
    return f"{x}_{y}"


def parseId(s: str):
    splitted = s.split("_")
    x = int(splitted[0])
    y = int(splitted[1])
    return x, y


def inBound(x, y, m):
    is_x_in = x >= 0 and x < len(m[0])
    is_y_in = y >= 0 and y < len(m)
    return is_x_in and is_y_in


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # global dx, dy
    visited = {}
    queue = deque()
    queue.appendleft(makeId(0, 0))
    result = []
    n_cols = len(matrix[0])
    n_rows = len(matrix)
    dx = 1
    dy = 0
    while len(queue) > 0:
        item = queue.popleft()
        x, y = parseId(item)
        visited[item] = True
        result.append(matrix[y][x])
        next_x, next_y = x + dx, y + dy
        next_id = makeId(next_x, next_y)
        # if visited.get(next_id) is None:
        if inBound(next_x, next_y, matrix) and visited.get(next_id) is None:
            queue.appendleft(next_id)
        else:
            # we need to check the bound
            cand_x = next_x
            cand_y = next_y
            while len(visited.keys()) < n_cols * n_rows:
                if dx == 1 and dy == 0:
                    cand_x, cand_y = x, y + 1
                    dx, dy = 0, 1
                elif dx == 0 and dy == 1:
                    cand_x, cand_y = x - 1, y
                    dx, dy = -1, 0
                elif dx == -1 and dy == 0:
                    cand_x, cand_y = x, y - 1
                    dx, dy = 0, -1
                elif dx == 0 and dy == -1:
                    cand_x, cand_y = x + 1, y
                    dx, dy = 1, 0
                cand_id = makeId(cand_x, cand_y)
                if inBound(cand_x, cand_y, matrix) and visited.get(cand_id) is None:
                    break

            # print(len(visited.keys()), n_cols * n_rows)
            if len(visited.keys()) < n_cols * n_rows:
                next_id = makeId(cand_x, cand_y)
                queue.appendleft(next_id)

    return result


if __name__ == "__main__":

    assert spiralOrder(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
            [21, 22, 23, 24],
        ]
    ) == [
        1,
        2,
        3,
        4,
        8,
        12,
        16,
        20,
        24,
        23,
        22,
        21,
        17,
        13,
        9,
        5,
        6,
        7,
        11,
        15,
        19,
        18,
        14,
        10,
    ]
    assert spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7,
    ]
