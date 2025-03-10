from typing import List


def findPeakElement(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    elif len(nums) == 2:
        if nums[0] > nums[1]:
            return 0
        return 1
    else:
        # since the ends are -inf we can confidently say any side will have a local maxima
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high + 1) // 2
            mid_val = nums[mid]
            left = mid - 1
            right = mid + 1
            left_val = -float("inf")
            right_val = -float("inf")
            if left >= 0:
                left_val = nums[left]
            if right < len(nums):
                right_val = nums[right]

            if mid_val > left_val and mid_val > right_val:
                return mid
            else:
                if left_val > mid_val:
                    high = mid - 1
                else:
                    low = mid
        return low

    # this is like a divide and conquer


if __name__ == "__main__":
    assert findPeakElement([1, 2, 3, 1]) == 2
    assert findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5
