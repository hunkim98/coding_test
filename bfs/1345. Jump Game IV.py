from collections import deque

# https://leetcode.com/problems/jump-game-iv/description/?envType=problem-list-v2&envId=9f2kyvf1


def minJumps(arr):
    # this is a dp question
    portal_dict = {}
    for i in range(len(arr)):
        item = arr[i]
        if portal_dict.get(item) is None:
            portal_dict[item] = [i]
        else:
            portal_dict[item].append(i)

    queue = deque([[0, 0]])  # queue will be an queue
    # with the first element as the current index
    # and the second element as the number of steps take
    visited = {}
    result = -1
    while len(queue) > 0:
        item = queue.popleft()
        idx = item[0]
        val = arr[idx]
        prev_step = item[1]
        visited[idx] = True

        if idx == len(arr) - 1:
            result = prev_step
            break

        # we can move in three ways
        # 1. move to right
        if idx + 1 < len(arr) and visited.get(idx + 1) is None:
            queue.append([idx + 1, prev_step + 1])
        # 2. move to left
        if idx - 1 >= 0 and visited.get(idx - 1) is None:
            queue.append([idx - 1, prev_step + 1])
        # 3. the most complex one, we can jump to the same number
        jumps = portal_dict[val]
        for jump_idx in jumps:
            if jump_idx == idx:
                continue
            if visited.get(jump_idx) is None:
                queue.append([jump_idx, prev_step + 1])
        portal_dict[val].clear()

    return result


if __name__ == "__main__":
    assert minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]) == 3
    assert minJumps([7]) == 0
    assert minJumps([7, 6, 9, 6, 9, 6, 9, 7]) == 1
