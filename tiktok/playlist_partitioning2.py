# Since the problem was getting max number
# the problem was a search problem (search a specific candidate)
# We used binary search for this question


def get_max_num_playlist(k, n, videoCategory):
    sum_videos = sum(videoCategory)
    low_bound = 0
    high_bound = sum_videos // k
    candidate = low_bound + high_bound
    while low_bound < high_bound:
        # we add 1 because we want to find the highest candidate
        candidate = (low_bound + high_bound + 1) // 2
        for i in range(n):
            acc_sum = 0
            acc_sum += videoCategory[i]
            if acc_sum >= candidate * k:
                break
        if acc_sum >= candidate * k:
            low_bound = candidate
        else:
            # acc_sum is lower than candidate * l
            # this means that the candidate is too high
            # we need to decrease the high bound
            high_bound = candidate - 1
    return low_bound


if __name__ == "__main__":
    assert get_max_num_playlist(3, 4, [1, 2, 2, 3]) == 2
    assert get_max_num_playlist(3, 9, [1, 2, 2, 2, 3, 3, 3, 3]) == 6
