# https://www.algoexpert.io/questions/Remove%20Islands

# First attempt

def removeIslands(matrix):
    
    def mark_not_island(x, y):
        if matrix[y][x] == 1:
            # 1 nodes not part of an island will be marked with the value 2
            matrix[y][x] = 2

            if y == 0: # top border
                # visits node below the current node if not on the top corners
                if x != 0 and x != len(matrix[0]) - 1:
                    mark_not_island(x, y+1)
            elif y == len(matrix) - 1: # bottom border
                # visits node above the current node if not on the bottom corners
                if x != 0 and x != len(matrix[0]) - 1:
                    mark_not_island(x, y-1)
            else:
                # visits nodes right of the current node if not on the left corners
                if x == 0: # left border
                    mark_not_island(x+1, y)
                # visits nodes adjacent to the current node
                elif x != 0 and x != len(matrix[0]) - 1:
                    mark_not_island(x+1, y)
                    mark_not_island(x-1, y)
                    mark_not_island(x, y+1)
                    mark_not_island(x, y-1)
                # visits node left of the current node if not on the right corners
                elif x == len(matrix[0]) - 1: # right border
                    mark_not_island(x-1, y)
        else:
            return

    # Unnecessary but may shorten O()T in these cases
    # Edge cases
    is_single_col = len(matrix) == 1
    is_single_row = len(matrix[0]) == 1
    is_dual_col = len(matrix) == 2
    is_dual_row = len(matrix[0]) == 2

    # In any of theses cases, the matrix cannot contain islands
    if is_single_col or is_dual_col or is_single_row or is_dual_row:
        return matrix

    # Finding the non-island 1 nodes (checking all borders)
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
            # nodes with the value 2 are restored to 1 nodes
            if matrix[y][x] == 2:
                matrix[y][x] = 1
            # any 1 nodes remaining are islands and are removed
            elif matrix[y][x] == 1:
                matrix[y][x] = 0
    
    return matrix


# Second solution
# Modified so only the nodes not on the borders are marked, 
# reducing the length of the end loop before returning the matrix

def removeIslands(matrix):

    def mark_not_island(x, y):
        if matrix[y][x] == 1:
            if y == 0:  # top border
                # visits node below the current node if not on the top corners
                if x != 0 and x != len(matrix[0]) - 1:
                    mark_not_island(x, y+1)
            elif y == len(matrix) - 1:  # bottom border
                # visits node above the current node if not on the bottom corners
                if x != 0 and x != len(matrix[0]) - 1:
                    mark_not_island(x, y-1)
            else:
                # visits nodes right of the current node if not on the left corners
                if x == 0:  # left border
                    mark_not_island(x+1, y)
                # visits nodes adjacent to the current node
                elif x != 0 and x != len(matrix[0]) - 1:
                    # 1 nodes not on any borders will be marked as not part of an island with the value 2
                    matrix[y][x] = 2
                    mark_not_island(x+1, y)
                    mark_not_island(x-1, y)
                    mark_not_island(x, y+1)
                    mark_not_island(x, y-1)
                # visits node left of the current node if not on the right corners
                elif x == len(matrix[0]) - 1:  # right border
                    mark_not_island(x-1, y)
        else:
            return

    # Unnecessary but may shorten O()T in these cases
    # Edge cases
    is_single_col = len(matrix) == 1
    is_single_row = len(matrix[0]) == 1
    is_dual_col = len(matrix) == 2
    is_dual_row = len(matrix[0]) == 2

    # In any of theses cases, the matrix cannot contain islands
    if is_single_col or is_dual_col or is_single_row or is_dual_row:
        return matrix

    # Finding the non-island 1 nodes (checking all borders)
    for y in range(len(matrix)):
        if y == 0 or y == len(matrix) - 1:  # top and bottom borders
            for x in range(len(matrix[y])):
                mark_not_island(x, y)
        else:
            x = 0  # left border
            mark_not_island(x, y)

            x = len(matrix[0]) - 1  # right border
            mark_not_island(x, y)

    # Modifying the matrix removing the 1 island nodes
    # Only looping through the "inner" matrix, ignoring the borders
    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[0]) - 1):
            # nodes with the value 2 are restored to 1 nodes
            if matrix[y][x] == 2:
                matrix[y][x] = 1
            # any 1 nodes remaining are islands and are removed
            elif matrix[y][x] == 1:
                matrix[y][x] = 0

    return matrix
