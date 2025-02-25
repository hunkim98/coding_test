def canReach(arr, start):
    # find the 0
    dest = {}

    for i in range(len(arr)):
        item = arr[i]
        if item == 0:
            dest[i] = True

    stack = []
    is_reachable = False
    stack.append(start)
    visited = {}
    # print(start, dest_idx)

    while len(stack) > 0 and is_reachable == False:
        item = stack.pop()
        if dest.get(item) is not None:
            is_reachable = True
            break
        jump = arr[item]
        visited[item] = True

        right = item + jump
        left = item - jump

        if right >= 0 and right < len(arr) and visited.get(right) is None:
            stack.append(right)

        if left >= 0 and left < len(arr) and visited.get(left) is None:
            stack.append(left)

    return is_reachable


if __name__ == "__main__":
    assert canReach([4, 2, 3, 0, 3, 1, 2], 5) == True
    assert canReach([4, 2, 3, 0, 3, 1, 2], 0) == True
    assert canReach([3, 0, 2, 1, 2], 2) == False
    assert canReach([0, 0], 0) == True
