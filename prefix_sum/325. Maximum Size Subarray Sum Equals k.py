def get_max_size_subarray_k(nums, k):
    acc_sums = []
    cur_sum = 0
    acc_sums_dict = {}
    for i in range(len(nums)):
        cur_sum += nums[i]
        acc_sums.append(cur_sum)
        if acc_sums_dict.get(cur_sum) is None:
            acc_sums_dict[cur_sum] = [i]
        else:
            acc_sums_dict[cur_sum].append(i)

    result = 0
    for right_i in range(len(acc_sums)):
        sum_till_right_i = acc_sums[right_i]
        if sum_till_right_i == k:
            result = max(result, right_i + 1)
        else:
            # This approach of finding 'sum_till_right_i - k' for finding sth is a 'two sum' algorithm
            does_left_i_exist = acc_sums_dict.get(sum_till_right_i - k) is not None
            if does_left_i_exist:
                left_i = acc_sums_dict[sum_till_right_i - k][0]  # get index value
                if left_i < right_i:
                    result = max(result, right_i - left_i)
    return result


if __name__ == "__main__":
    assert get_max_size_subarray_k([1, -1, 5, -2, 3], 3) == 4
    assert get_max_size_subarray_k([-2, -1, 2, 1], 1) == 2
