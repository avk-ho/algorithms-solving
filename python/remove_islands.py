# https://www.algoexpert.io/questions/Remove%20Islands

# First attempt

def removeIslands(matrix):
    
    def mark_not_island(x, y):
        if matrix[y][x] == 1:
            matrix[y][x] = 2

            if y == 0: # top border
                if x != 0 and x != len(matrix[0]) - 1:
                    mark_not_island(x, y+1)
                    return
            elif y == len(matrix) - 1: # bottom border
                if x != 0 and x != len(matrix[0]) - 1:
                    mark_not_island(x, y-1)
                    return
            else:
                if x == 0: # left border
                    mark_not_island(x+1, y)
                elif x != 0 and x != len(matrix[0]) - 1:
                    mark_not_island(x+1, y)
                    mark_not_island(x-1, y)
                    mark_not_island(x, y+1)
                    mark_not_island(x, y-1)
                    return
                elif x == len(matrix[0]) - 1: # right border
                    mark_not_island(x-1, y)
        else:
            return

    # Edge cases
    is_single_col = len(matrix) == 1
    is_single_row = len(matrix[0]) == 1
    is_dual_col = len(matrix) == 2
    is_dual_row = len(matrix[0]) == 2

    if is_single_col or is_dual_col or is_single_row or is_dual_row:
        return matrix

    # Finding the non-island 1 nodes
    for y in range(len(matrix)):
        if y == 0 or y == len(matrix) - 1: # top and bottom borders
            for x in range(len(matrix[y])):
                mark_not_island(x, y)
        else:
            x = 0 # left border
            mark_not_island(x, y)
            
            x = len(matrix[0]) - 1 # right border
            mark_not_island(x, y)

    # Modifying the matrix removing the 1 island nodes
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 2:
                matrix[y][x] = 1
            elif matrix[y][x] == 1:
                matrix[y][x] = 0
    
    return matrix

