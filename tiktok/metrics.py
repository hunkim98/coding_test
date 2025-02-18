# financial Metrics
def getMaxGoodSubarrayLength(n, limit, financialMetrics):
    low_bound = limit / len(financialMetrics)
    result = 0
    for item in financialMetrics:
        if item > low_bound:
            result += 1
    return result


if __name__ == "__main__":
    assert getMaxGoodSubarrayLength(5, 6, [1, 3, 4, 3, 1]) == 3
