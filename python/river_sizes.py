# https://www.algoexpert.io/questions/River%20Sizes

# First attempt
def riverSizes(matrix):
    def mesureRiver(matrix, x, y, river_length):
        if matrix[y][x] == 1:
            river_length += 1
            matrix[y][x] = 0
            
            if x == 0:
                if y == 0: # top left
                    mesureRiver(matrix, x+1, y, river_length)
                    mesureRiver(matrix, x, y+1, river_length)
                elif y != 0 and y < len(matrix)-1: # left border
                    mesureRiver(matrix, x+1, y, river_length)
                    mesureRiver(matrix, x, y+1, river_length)
                    mesureRiver(matrix, x, y-1, river_length)
                else: # y == len(matrix)-1 # bottom left
                    mesureRiver(matrix, x, y+1, river_length)
                    mesureRiver(matrix, x+1, y, river_length)

            elif x != 0 and x < len(matrix[0])-1:
                if y == 0: # top border
                    mesureRiver(matrix, x+1, y, river_length)
                    mesureRiver(matrix, x-1, y, river_length)
                    mesureRiver(matrix, x, y+1, river_length)
                elif y != 0 and y < len(matrix)-1: # center
                    mesureRiver(matrix, x+1, y, river_length)
                    mesureRiver(matrix, x-1, y, river_length)
                    mesureRiver(matrix, x, y+1, river_length)
                    mesureRiver(matrix, x, y-1, river_length)
                else:  # y == len(matrix)-1 # bottom border
                    mesureRiver(matrix, x+1, y, river_length)
                    mesureRiver(matrix, x-1, y, river_length)
                    mesureRiver(matrix, x, y-1, river_length)
    
            else: # x == len(matrix[0])-1
                if y == 0: # top right
                    mesureRiver(matrix, x-1, y, river_length)
                    mesureRiver(matrix, x, y+1, river_length)
                elif y != 0 and y < len(matrix)-1: # right border
                    mesureRiver(matrix, x-1, y, river_length)
                    mesureRiver(matrix, x, y+1, river_length)
                    mesureRiver(matrix, x, y-1, river_length)
                else: # y == len(matrix)-1 # bottom right
                    mesureRiver(matrix, x-1, y, river_length)
                    mesureRiver(matrix, x, y-1, river_length)

            return river_length

    river_sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                river_length = 0
                river_sizes.append(mesureRiver(matrix, i, j, river_length))
    
    return river_sizes

# [X, X, X, X, X]
# [X, X, X, X, X]
# [X, X, X, X, X]
# [X, X, X, X, X]
# [X, X, X, X, X]

# Incomplete

# Second attempt
def riverSizes(matrix):
    def mesure_river(x, y):
        if matrix[y][x] == 1:
            matrix[y][x] = 0

            # Edge cases
            if is_single_row and is_single_col: # 1*1 matrix
                return 1
            elif is_single_row:
                if x == len(matrix[0]) - 1:
                    return 1
                else:
                    return 1 + mesure_river(x+1, y)
            elif is_single_col:
                if y == len(matrix) - 1:
                    return 1
                else:
                    return 1 + mesure_river(x, y+1)
            

            if y == 0: # top border
                if x == len(matrix[0]) - 1: # right border # top-right corner
                    return 1 + mesure_river(x, y+1)
                else:
                    return 1 + mesure_river(x+1, y) + mesure_river(x, y+1)

            elif y < len(matrix) - 1:
                if x == 0: # left border
                    return 1 + mesure_river(x+1, y) + mesure_river(x, y-1) + mesure_river(x, y+1)
                elif x == len(matrix[0]) - 1: # right border
                    return 1 + mesure_river(x-1, y) + mesure_river(x, y-1) + mesure_river(x, y+1)
                elif x < len(matrix[0]) - 1:
                    return 1 + mesure_river(x-1, y) + mesure_river(x+1, y) + mesure_river(x, y-1) + mesure_river(x, y+1)
            
            elif y == len(matrix) - 1: # bottom border
                if x == 0: # left border # bottom-left corner
                    return 1 + mesure_river(x+1, y) + mesure_river(x, y-1)
                elif x == len(matrix[0]) - 1: # right border # bottom-right corner
                    return 1 + mesure_river(x-1, y) + mesure_river(x, y-1)
                elif x < len(matrix[0]) - 1:
                    return 1 + mesure_river(x-1, y) + mesure_river(x+1, y) + mesure_river(x, y-1)
                

        else:
            return 0
    
    is_single_row = len(matrix) == 1
    is_single_col = len(matrix[0]) == 1
    rivers_length = []
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 1:
                rivers_length.append(mesure_river(x, y))
    
    return rivers_length

# Recursive solution, very unoptimized, may go through the same coordinates multiple times