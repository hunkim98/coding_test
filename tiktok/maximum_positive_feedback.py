import heapq


def maximize_feedback(size, feedback):
    streak = []
    heapq.heapify([])

    combo = 0
    result = 0
    max_combo = -1
    for i in range(len(feedback)):
        item = feedback[i]
        if item == "0":
            result += 1
            if combo > max_combo:
                max_combo = combo
            combo = 0  # reset
        elif item == "1":
            combo += 1
    result += max_combo
    return result


if __name__ == "__main__":
    assert maximize_feedback(6, "100110") == 5
 