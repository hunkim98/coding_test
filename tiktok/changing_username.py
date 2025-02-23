def get_total_distinct_usernames(name):
    # change "cc" to 'a'
    # change "dd" to 'b'
    # this is dp
    # T(n) = T(n-1) + T(n-2)
    n = len(name)

    fib = [0] * (n + 2)
    fib[0] = 0
    fib[1] = 1
    fib[2] = 2
    for i in range(3, n + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    M = 10**9 + 7
    i = 0
    result = 1
    while i < n:
        char = name[i]
        c_streak = 0
        while char == "c":
            c_streak += 1
            i += 1
            if i >= n:
                break
            char = name[i]

        if c_streak != 0:
            result = result * fib[c_streak] % M
            print(result, "c_streak", c_streak)

        d_streak = 0
        while char == "d" and i < n:
            d_streak += 1
            i += 1
            if i >= n:
                break
            char = name[i]

        if d_streak != 0:
            result = result * fib[d_streak] % M

        i += 1
    return result


if __name__ == "__main__":
    assert get_total_distinct_usernames("ccc") == 3
