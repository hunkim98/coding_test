# This is a dynamic programming problem
def longest_common_substring(n1, n2):
    str1 = str(n1)  # this will be column length
    str2 = str(n2)  # this will be row length
    print(str1, str2)
    dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
    # the dp index means how many items from n1 or n2 have been used
    # dp[1][1] means what is the lcs length when the first two characters were used
    # print(len(dp), str2, len(dp[0]), str1)
    max_j = -1
    max_i = -1
    max_len = -1
    for j in range(1, len(str2) + 1):  # str2 is row length
        for i in range(1, len(str1) + 1):  # str1 is column length
            if str1[i - 1] == str2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1] + 1
                if dp[j][i] > max_len:
                    max_len = dp[j][i]
                    max_j = j
                    max_i = i
            else:
                dp[j][i] = 0
            # this is for simple count of sum
    sequence = ""

    i = max_i
    j = max_j
    while dp[j][i] != 0:
        sequence = str1[i - 1] + sequence
        i -= 1
        j -= 1

    print(sequence)

    return max_len

    # pass


if __name__ == "__main__":
    assert longest_common_substring(12344455521, 34215662) == 2  # 34
    assert longest_common_substring(2345, 123) == 2  # 23
