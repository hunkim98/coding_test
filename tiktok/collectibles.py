def primeNumbersTill(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [idx for idx in range(2, n + 1) if primes[idx] == True]


def divideCardPackets(inputs):
    primes = primeNumbersTill(500)
    minSum = float("inf")
    for p in primes:
        sum = 0
        for val in inputs[1:]:
            sum += val % p
        if sum < minSum:
            minSum = sum

    return minSum


if __name__ == "__main__":
    assert divideCardPackets([5, 3, 8, 7, 6, 4]) == 2
    assert divideCardPackets([6, 3, 9, 7, 6, 5, 2]) == 4
    # assert divideCardPackets([7, 7, 7, 7, 7, 7, 7]) == 0
    print(primeNumbersTill(20))
