from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # first find row position
    rows_start = []
    for row in matrix:
        rows_start.append(row[0])

    row_low = 0
    row_high = len(matrix) - 1
    while row_low < row_high:
        mid = (row_low + row_high + 1) // 2
        mid_val = rows_start[mid]

        if target >= mid_val:
            row_low = mid
        else:
            row_high = mid - 1

    row_idx = row_low
    if target >= rows_start[row_low]:
        row_idx = row_low
    else:
        row_idx = row_low - 1

    col = matrix[row_idx]
    col_low = 0
    col_high = len(col) - 1

    while col_low <= col_high:
        mid = (col_low + col_high) // 2
        mid_val = col[mid]

        if target == mid_val:
            return True

        if target > mid_val:
            col_low = mid + 1
        else:
            col_high = mid - 1

    return False


if __name__ == "__main__":
    assert searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True
    assert searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False
