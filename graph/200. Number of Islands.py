from typing import List
from collections import deque


def makeId(x, y):
    return f"{x}_{y}"


def parseId(str):
    spl = str.split("_")
    return int(spl[0]), int(spl[1])


def bounded(x, y, grid):
    y_bounded = y >= 0 and y < len(grid)
    x_bounded = x >= 0 and x < len(grid[0])
    return x_bounded and y_bounded


dir_y = [1, 0, -1, 0]  # up, right, down, left
dir_x = [0, 1, 0, -1]


def numIslands(grid: List[List[str]]) -> int:
    visited = {}
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            id = makeId(x, y)
            if grid[y][x] == "0":
                continue
            if visited.get(id) is not None:
                continue

            queue = deque()
            queue.appendleft(id)
            # print(id)
            while len(queue) > 0:
                item = queue.popleft()
                visited[item] = True
                org_x, org_y = parseId(item)
                for i in range(4):
                    new_x, new_y = org_x + dir_x[i], org_y + dir_y[i]

                    if not bounded(new_x, new_y, grid):
                        continue
                    # print(item, new_x, new_y)

                    new_id = makeId(new_x, new_y)

                    if visited.get(new_id) is not None:
                        continue

                    if grid[new_y][new_x] == "1":
                        queue.appendleft(new_id)

            result += 1
    return result


if __name__ == "__main__":
    assert (
        numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
