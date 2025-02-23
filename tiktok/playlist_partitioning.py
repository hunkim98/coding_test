def get_max_num_playlist(k, n, videoCategory):
    sort_category = sorted(videoCategory)  # this is ascending
    transformed_num = 0
    for i in range(len(sort_category) - 1, -1, -1):
        transformed_num += sort_category[i] * (10**i)

    subtract_by = 0
    for i in range(k):
        subtract_by += 10**i

    playlists = 0
    while n >= k:
        # we need to check
        transformed_num -= subtract_by
        while transformed_num % 10 == 0:
            transformed_num /= 10
            n -= 1
        playlists += 1

    return playlists


if __name__ == "__main__":
    assert get_max_num_playlist(3, 4, [1, 2, 2, 3]) == 2
    assert get_max_num_playlist(3, 9, [1, 2, 2, 2, 3, 3, 3, 3]) == 6
