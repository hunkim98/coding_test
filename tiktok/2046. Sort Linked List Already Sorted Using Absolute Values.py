def getSortedList(head):
    left_list = []
    right_list = []
    for i in range(len(head) - 1, -1, -1):
        item = head[i]
        if item > 0:
            right_list.append(item)
        else:
            left_list.append(item)

    for i in range(len(right_list) - 1, -1, -1):
        item = right_list[i]
        left_list.append(item)

    return left_list


if __name__ == "__main__":
    assert getSortedList([0, 2, -5, 5, 10, -10]) == [-10, -5, 0, 2, 5, 10]
    assert getSortedList([0, 1, 2]) == [0, 1, 2]
    assert getSortedList([1]) == [1]
