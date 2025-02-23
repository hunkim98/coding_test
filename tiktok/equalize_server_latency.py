import math

result = 0


# this gives total cost
def dfs(i, n, latency):
    global result
    # latency is the edges
    if i >= n:
        return 0

    lcost = dfs(2 * i + 1, n, latency)
    rcost = dfs(2 * i + 2, n, latency)
    result += abs(rcost - lcost)
    return max(lcost, rcost) + latency[i]


def minAdditionalLatency(n, latency):
    dfs(0, n - 1, latency)
    return result


if __name__ == "__main__":
    assert minAdditionalLatency(3, [10, 5]) == 5
