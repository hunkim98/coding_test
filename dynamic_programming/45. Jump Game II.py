def getMinJumps(nums):
    # we will use dp
    # dp[pos] will be the value of how many jumps it takes to go from
    # pos to end
    dp = [float("inf")] * len(nums)
    # we know only one result
    dp[len(nums) - 1] = 0  # from n-1, there is no need to jump

    for i in range(len(nums) - 2, -1, -1):
        # this means it is too big
        if i + nums[i] >= len(nums) - 1:
            dp[i] = 1
        else:
            for j in range(nums[i] + i, i, -1):
                # for j in range(i, nums[i] + i + 1):
                # we will constantly dp[i]
                # the dp[i] should be based on the best dp[j] among dp[i]'s reach
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[0]


if __name__ == "__main__":
    assert getMinJumps([2, 3, 1, 1, 4]) == 2
    assert getMinJumps([2, 3, 0, 1, 4]) == 2
    assert getMinJumps([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 2
