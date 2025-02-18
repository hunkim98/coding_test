# This is a dynamic programming problem
def longest_common_subsequence(n1, n2):
    str1 = str(n1)  # this will be column length
    str2 = str(n2)  # this will be row length
    print(str1, str2)
    dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
    # the dp index means how many items from n1 or n2 have been used
    # dp[1][1] means what is the lcs length when the first two characters were used
    # print(len(dp), str2, len(dp[0]), str1)
    for j in range(1, len(str2) + 1):  # str2 is row length
        for i in range(1, len(str1) + 1):  # str1 is column length
            if str1[i - 1] == str2[j - 1]:
                print("column", i - 1, "row", j - 1, str1[i - 1])
                dp[j][i] = dp[j - 1][i - 1] + 1
            else:
                dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
            # this is for simple count of sum
    sequence = ""
    i = len(str1)
    j = len(str2)
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            sequence = str1[i - 1] + sequence
            i -= 1
            j -= 1
        else:
            if dp[j][i - 1] > dp[j - 1][i]:
                i -= 1
            else:
                j -= 1
    print(sequence)
    print(dp[len(str2)][len(str1)])

    return dp[len(str2)][len(str1)]

    # pass


if __name__ == "__main__":
    assert longest_common_subsequence(12344455521, 34215662) == 4
    assert longest_common_subsequence(2345, 123) == 2
