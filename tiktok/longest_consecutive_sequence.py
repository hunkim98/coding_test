# unsorted array of integers nums
def find_longest_consecutive_sequence(nums):
    dictionary = {}
    for item in nums:
        if dictionary.get(item) is None:
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    unique = sorted(dictionary.keys())
    result = 0
    cur_sum = 0
    for i in range(len(unique)):
        cur_item = unique[i]
        cur_sum += dictionary[cur_item]
        if cur_sum > result:
            result = cur_sum
        if i + 1 == len(unique):
            break
        next_item = unique[i + 1]
        if next_item - cur_item != 1:
            cur_sum = 0

    return result


if __name__ == "__main__":
    assert find_longest_consecutive_sequence([5, 5, 2, 4, 1, 6, 2]) == 4
