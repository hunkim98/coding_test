# each box has the number of fish
# 0) fish add
# put one fish in the acquarium that has least amount (multiple smallest - each put in one)
# 1) Stack
# stack the box from left
# box with more than 2 stories are pulled up and turned 90 degrees clockwise
# we do this untill the height of the pulled up boxes exceeds the leftover
# 2) fish control
# check all neighbors # simulataneous moment based
# diff of neighboring and then 5 나누기 0 초과 d이면 d만큼 전달
# 3) Lay Down
# from left to right. down to up
# after finished stacking we flatten each
# 4) Stack again
# this time split into half. and then turn the left upside down and stack
# we do this two times.
# 5) fish control again
# 6) Lay down again

# N is box count.
# K is required difference between least and biggest
# how many times to make diff less than K
N, K = map(int, input().split())
boxes = [int(x) for x in input().split()]


def add_fish_to_min(boxes):
    smallest = 100_000
    for i in range(len(boxes)):
        value = boxes[i]
        if value < smallest:
            smallest = value

    for i in range(len(boxes)):
        value = boxes[i]
        if value == smallest:
            # add one fish to the boxes with least fish
            boxes[i] += 1


def stack_from_left(boxes):
    temp = {"level0": boxes.copy()}
    # while len(temp["level0"])
    # len(temp) means the number of keys in dictionary
    # temp.keys() mean the height of the stacks
    single_stack_boxes = len(boxes)
    while single_stack_boxes > len(temp.keys()):
        curr_level = len(temp.keys())
        prev_level = curr_level - 1
        if curr_level == 1:
            boxes_to_move = 1
            curr_level_key = "level" + str(0)
            new_level_key = "level" + str(1)
            new_level_box = temp[curr_level_key][:curr_level]
            curr_level_box = temp[curr_level_key][curr_level:]
            temp[curr_level_key] = curr_level_box
            temp[new_level_key] = new_level_box
        else:
            top_level_box_count = len(temp["level" + str(total_levels - 1)])
            total_levels = len(temp.keys())
            extracted_boxes = []
            for i in range(total_levels):
                curr_level_key = "level" + str(i)
                extract_from_level = temp[curr_level_key][:top_level_box_count]
                extracted_boxes.append(extract_from_level)
                # the bottom level should have its numbers deleted
                if i == 0:
                    # reform the original level
                    temp[curr_level_key] = temp[curr_level_key][top_level_box_count:]
            # now that we have the extracted_boxes array, we have to flip it [[3], [5]] to [[3, 5]] : 2x1 to 1x2
            # ex2: [[3,14], [3,5]] -> [[14,5], [3,3]]
            # [[9,3],[14,5], [3,3]] -> [[3,5,3], [9,14,3]]
            # left col becomes top row, right col becomes bottom row
            # we operate the matrix
            stacks = []
            for i in range(top_level_box_count):
                col = []
                for j in range(len(extracted_boxes)):
                    col.append(extracted_boxes[j][i])  # col = [14, 55]
                stacks.append(col)
            stacks = list(reversed(stacks))
            for i in range(len(stacks)):
                level_key = "level" + str(i + 1)
                temp[level_key] = stacks[i]
        total_levels = len(temp.keys())
        top_level_box_count = len(temp["level" + str(total_levels - 1)])
        single_stack_boxes = single_stack_boxes - top_level_box_count
    return temp


def fish_control(level_dict):
    total_level = len(level_dict.keys())
    temp = {}
    # initialize
    for key in level_dict.keys():
        temp[key] = level_dict[key].copy()
    for i in reversed(range(total_level)):
        curr_level = "level" + str(i)
        up_level = "level" + str(i + 1)
        bottom_level = "level" + str(i - 1)
        curr_boxes = level_dict[curr_level]
        for j in range(len(curr_boxes)):
            curr = level_dict[curr_level][j]
            up = None
            if up_level in level_dict:
                level_length = len(level_dict[up_level])
                if j >= 0 and j < level_length:
                    up = level_dict[up_level][j]
            left = None
            if j - 1 >= 0 and j - 1 < len(curr_boxes):
                left = curr_boxes[j-1]
            bottom = None
            if bottom_level in level_dict:
                level_length = len(level_dict[bottom_level])
                if j >= 0 and j < level_length:
                    bottom = level_dict[bottom_level][j]
            right = None
            if j + 1 >= 0 and j + 1 < len(curr_boxes):
                right = curr_boxes[j+1]

            if up and curr < up:
                diff = up - curr
                d = diff // 5
                if d > 0:
                    temp[up_level][j] -= d
                    temp[curr_level][j] += d
            if left and curr < left:
                diff = left - curr
                d = diff // 5
                if d > 0:
                    temp[curr_level][j - 1] -= d
                    temp[curr_level][j] += d
            if bottom and curr < bottom:
                diff = bottom - curr
                d = diff // 5
                if d > 0:
                    temp[bottom_level][j] -= d
                    temp[curr_level][j] += d
            if right and curr < right:
                diff = right - curr
                d = diff // 5
                if d > 0:
                    temp[curr_level][j + 1] -= d
                    temp[curr_level][j] += d
    return temp


def flatten(controlled_dict):
    # left to right, bottom to up
    bottom_level_length = len(controlled_dict["level0"])
    total_levels = len(controlled_dict.keys())
    flattened = []
    for i in range(bottom_level_length):
        # we extract index from each level
        for j in range(total_levels):
            level_key = "level" + str(j)
            if level_key in controlled_dict:
                level_boxes = controlled_dict[level_key]
                if i >= 0 and i < len(level_boxes):
                    flattened.append(level_boxes[i])
    return flattened


def stack_from_mid(flattened_list):
    init_len = len(flattened_list)
    first_div = int(init_len / 2)
    second_div = int(first_div / 2)
    temp = {}
    # first step
    first_half = flattened_list[:first_div]
    second_half = flattened_list[first_div:]
    first_half = list(reversed(first_half))

    n_bottom_half = second_half[second_div:]
    n_top_half = second_half[:second_div]
    n_top_half = list(reversed(n_top_half))
    n_second_half = first_half[second_div:]
    n_third_half = first_half[:second_div]
    n_third_half = list(reversed(n_third_half))

    temp["level0"] = n_bottom_half
    temp["level1"] = n_second_half
    temp["level2"] = n_third_half
    temp["level3"] = n_top_half
    return temp


#
def main():
    s_boxes = boxes
    shifted = 0
    while not max(s_boxes) - min(s_boxes) <= K:
        add_fish_to_min(s_boxes)
        level_dict = stack_from_left(s_boxes)
        controlled_dict = fish_control(level_dict)
        flattened = flatten(controlled_dict)
        stacked = stack_from_mid(flattened)
        control_again_dict = fish_control(stacked)
        s_boxes = flatten(control_again_dict)
        shifted += 1
    print(shifted)


main()
