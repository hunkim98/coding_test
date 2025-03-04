def hIndex(citations):
    sorted_citation = sorted(citations)
    min_cite = sorted_citation[0]
    max_cite = sorted_citation[len(citations) - 1]

    acc_citation = 0
    less_or_equal_than = {}
    acc_key = max_cite
    result = -1
    for i in range(len(sorted_citation) - 1, -1, -1):
        item = sorted_citation[i]
        if acc_key != item:
            less_or_equal_than[acc_key] = acc_citation
            potential = min(acc_key, acc_citation)
            if result < potential:
                result = potential
            acc_key = item
        acc_citation += 1

    less_or_equal_than[min_cite] = acc_citation
    potential = min(min_cite, acc_citation)
    if result < potential:
        result = potential

    return result


if __name__ == "__main__":
    assert hIndex([1, 3, 1]) == 1
    assert hIndex([3, 0, 6, 1, 5]) == 3
    assert hIndex([100]) == 1
