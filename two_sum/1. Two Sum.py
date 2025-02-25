def get_two_sum_indices(nums, target):
    nums_dict = {}
    for i in range(len(nums)):
        item = nums[i]
        if nums_dict.get(item) is None:
            nums_dict[item] = [i]
        else:
            nums_dict[item].append(i)

    for i in range(len(nums)):
        item = nums[i]
        comp = target - item
        if nums_dict.get(comp):
            for index in nums_dict.get(comp):
                if index != i:
                    if index > i:
                        return [i, index]
                    else:
                        return [index, i]


if __name__ == "__main__":
    assert get_two_sum_indices([2, 7, 11, 15], 9) == [0, 1]
    assert get_two_sum_indices([3, 2, 4], 6) == [1, 2]
    assert get_two_sum_indices([3, 3], 6) == [0, 1]
