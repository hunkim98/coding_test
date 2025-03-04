def hIndex(citations):
    citations.sort()
    n = len(citations)
    low, high = 0, n - 1
    ans = 0

    while low < high:
        mid = (low + high + 1) // 2  # Rounds up

        if citations[mid] >= n - mid:
            # citations[mid] is large enough for h = n - mid
            ans = max(ans, n - mid)
            high = mid - 1  # try to find a larger h-index to the left
        else:
            low = mid  # move right

    # After the loop, low == high or low just passed high.
    # We must check one last time at index `low`.
    # print(ans)
    if citations[low] >= n - low:
        ans = max(ans, n - low)
    return ans


if __name__ == "__main__":
    assert hIndex([100]) == 1
    assert hIndex([0, 0, 2]) == 1
    # 0, 0, 2
    # (0+2+1)//2 = 1
    #
    assert hIndex([1, 3, 1]) == 1
    # 1, 1, 3
    # (0+2+1)//2 = 1
    assert hIndex([3, 0, 6, 1, 5]) == 3
    # 0, 1, 3, 5, 6
