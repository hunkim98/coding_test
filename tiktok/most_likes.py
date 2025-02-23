def get_max_likes(prediction):
    # this is a dp
    likes = {}
    max_item = -1
    for item in prediction:
        if likes.get(item) is None:
            likes[item] = item
            if item > max_item:
                max_item = item
        else:
            likes[item] += item

    # not we create a dp
    dp = [0]

    result = 0
    for i in range(1, max_item + 1):
        max_likes = 0
        if likes.get(i) is None:
            max_likes = dp[i - 1]
        else:
            if likes.get(i - 1) is None:
                max_likes = dp[i - 1] + likes.get(i)
            else:
                max_likes = dp[i - 2] + likes.get(i)
        if max_likes > result:
            result = max_likes
        dp.append(max_likes)
    # print(result, dp)
    return result


if __name__ == "__main__":
    assert get_max_likes([1, 2, 3, 3, 3, 4, 4]) == 10
