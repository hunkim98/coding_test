from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    # already sorted in non decreasing order
    # find two numbers such taht they add up to a specific target number
    # return indices of the two numbers
    nums_dict = {}
    for i in range(len(numbers)):
        num = numbers[i]
        if nums_dict.get(num) is None:
            nums_dict[num] = [i]
            continue
        if len(nums_dict[num]) >= 2:
            continue
        nums_dict[num].append(i)

    for key in nums_dict.keys():
        key_index = nums_dict[key][0]
        comp_num = target - key
        if nums_dict.get(comp_num) is None:
            continue

        if comp_num == key:
            if len(nums_dict[comp_num]) >= 2:
                return [key_index + 1, nums_dict[comp_num][1] + 1]
            else:
                continue

        return [key_index + 1, nums_dict[comp_num][0] + 1]


if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == [1, 2]
