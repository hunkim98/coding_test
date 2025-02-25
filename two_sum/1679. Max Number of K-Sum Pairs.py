def get_max_num_k_sum_pairs(nums, k):
    operations = 0
    nums_dict = {}
    for i in range(len(nums)):
        item = nums[i]
        if nums_dict.get(item) is None:
            nums_dict[item] = 1
        else:
            nums_dict[item] += 1

    for key in nums_dict.keys():
        item = key
        comp = k - item

        if nums_dict.get(item) is not None and nums_dict.get(comp) is not None:
            if item == comp:
                # we need to remove both
                operations += nums_dict[item] // 2
            else:
                if nums_dict[item] >= 1 and nums_dict[comp] >= 1:
                    pair_cnt = min(nums_dict[item], nums_dict[comp])
                    nums_dict[item] -= pair_cnt
                    nums_dict[comp] -= pair_cnt
                    operations += pair_cnt
    return operations


if __name__ == "__main__":
    assert get_max_num_k_sum_pairs([1, 2, 3, 4], 5) == 2
    assert get_max_num_k_sum_pairs([3, 1, 3, 4, 3], 6) == 1
