def getMinJumps(nums):
    # guaranteed that you can reach nums[n-1]
    # just choose max along the way
    # dp[i][j]
    # i means the numbers considered
    # j means the reachable index
    # dp[i][j] will be the minimum mump count to reach j
    # we need to check everything
    i = 0
    max_reach = 0
    last_jump_pos = 0

    jump_cnt = 0

    while last_jump_pos < len(nums) - 1:
        max_reach = max(max_reach, i + nums[i])
        if i == last_jump_pos:
            # this means we need to update our last_jump_pos to our current max reach
            last_jump_pos = max_reach
            # since we moved our jump pos we need to add it to our jump count
            jump_cnt += 1
        i += 1
    return jump_cnt


if __name__ == "__main__":
    assert getMinJumps([2, 3, 1, 1, 4]) == 2
    assert getMinJumps([2, 3, 0, 1, 4]) == 2
    assert getMinJumps([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 2
