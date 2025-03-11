def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    left = 0
    occr = {}
    var_cnt = 0
    for right in range(len(s)):
        item = s[right]
        if occr.get(item) is None:
            occr[item] = 1
        else:
            occr[item] += 1
        if occr[item] == 1:
            var_cnt += 1
        elif occr[item] > 1:
            var_cnt -= 1
        if var_cnt == right - left + 1:
            max_length = max(max_length, var_cnt)
        # there should be unsatifsfied condition
        while left < right and var_cnt < right - left:
            left_item = s[left]
            occr[left_item] -= 1
            if occr[item] == 1:
                var_cnt += 1
            else:
                var_cnt -= 1
            if var_cnt == right - left + 1:
                max_length = max(max_length, var_cnt)
            left += 1

    return max_length


if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
