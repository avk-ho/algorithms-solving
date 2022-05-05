# https://www.algoexpert.io/questions/Search%20In%20Sorted%20Matrix

# First solution
def searchInSortedMatrix(matrix, target):
    target_row_idx = 0
    target_col_idx = len(matrix[0]) - 1

    while matrix[target_row_idx][target_col_idx] != target and target_col_idx >= 0 and target_row_idx < len(matrix):
        current_value = matrix[target_row_idx][target_col_idx]
        # print(current_value)
        if current_value > target:
            target_col_idx -= 1
        elif current_value < target:
            target_row_idx += 1

    if matrix[target_row_idx][target_col_idx] == target:
        return [target_row_idx, target_col_idx]
    else:
        return [-1, -1]

# 1 2 3 4
# 5 6 7 8
# 7-2 / 4-2

# Cleaning solution
def searchInSortedMatrix(matrix, target):
    target_row_idx = 0
    target_col_idx = len(matrix[0]) - 1

    while target_col_idx >= 0 and target_row_idx < len(matrix):
        current_value = matrix[target_row_idx][target_col_idx]
        
        if current_value > target:
            target_col_idx -= 1
        elif current_value < target:
            target_row_idx += 1
        else:
            return [target_row_idx, target_col_idx]

    return [-1, -1]