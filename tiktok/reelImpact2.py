import heapq


# lined list problem


def getTotalImpact(initialReelImpacts, newReelImpacts, k):
    m = len(initialReelImpacts)
    n = len(newReelImpacts)
    sorted_init = sorted(initialReelImpacts)

    filtered = sorted_init[m - k :]

    heapq.heapify(filtered)  # automatically a min heap

    result = filtered[0]
    for i in range(n):
        item = newReelImpacts[i]

        heapq.heappush(filtered, item)
        heapq.heappop(filtered)

        result += filtered[0]

    return result


if __name__ == "__main__":
    assert getTotalImpact([2, 3], [4, 5, 1], 2) == 13
    assert getTotalImpact([3, 3], [4, 5, 1], 2) == 14
