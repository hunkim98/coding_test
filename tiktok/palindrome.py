def isPalindrome(n):
    string = str(n)
    result = True

    for i in range(len(string)):
        k = len(string) - i - 1  # this is the end
        if i == k or i > k:
            break
        i_word = string[i]
        k_word = string[k]

        if i_word != k_word:
            result = False
            break
    return result


if __name__ == "__main__":
    assert isPalindrome(12321) == True
    assert isPalindrome(1234544444333333334444454321) == True
