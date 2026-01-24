from typing import List


def maxArea(height: List[int]) -> int:
    # two sum
    low = 0
    high = len(height) - 1
    result = 0
    while low < high:
        w = high - low
        h = min(height[low], height[high])
        fill = w * h
        if fill > result:
            result = fill
        if height[low] > height[high]:
            high -= 1
        else:
            low += 1
    return result


if __name__ == "__main__":
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert maxArea([1, 1]) == 1
