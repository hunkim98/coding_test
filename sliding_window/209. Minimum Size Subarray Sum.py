# Sliding Window Problem
# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4502/


# When coding question specifice a subarray, it must maintain the original order of elements
def get_min_size_subarray(target, nums):
    sum = 0

    left_i = 0
    min_size = float("inf")
    for right_i in range(len(nums)):
        # right_i will move
        sum += nums[right_i]
        while sum >= target and left_i <= right_i:
            # we will only progress left_i when we need to remove
            # if sum is bigger than target, because we are trying to find min_size
            # we will try to erase the left number to check if the sum can still be bigger than target
            min_size = min(min_size, right_i - left_i + 1)
            sum -= nums[left_i]
            left_i += 1

    # print(min_size)
    if min_size == float("inf"):
        return 0
    return min_size


if __name__ == "__main__":
    assert get_min_size_subarray(7, [2, 3, 1, 2, 4, 3]) == 2
    assert get_min_size_subarray(4, [1, 4, 4]) == 1
    assert (
        get_min_size_subarray(
            11,
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
        )
        == 0
    )
