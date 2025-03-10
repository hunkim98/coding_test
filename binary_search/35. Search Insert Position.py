from typing import List


def searchInsert(nums: List[int], target: int):
    # the array is already sorted
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high + 1) // 2
        mid_val = nums[mid]
        if mid_val == target:
            return mid

        if target > mid_val:
            low = mid
        else:
            high = mid - 1
    if target > nums[low]:
        return low + 1
    else:
        return low


if __name__ == "__main__":
    assert searchInsert([1, 3, 5, 6], 5) == 2
    assert searchInsert([1, 3, 5, 6], 2) == 1
    assert searchInsert([1, 3, 5, 6], 7) == 4
