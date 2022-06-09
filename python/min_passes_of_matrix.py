# https://www.algoexpert.io/questions/minimum-passes-of-matrix

# return the number of "passes" needed to convert all numbers into positives
# or -1 if impossible

# First attempt
def minimumPassesOfMatrix(matrix):

    def checkAdjacentNum(x_coor, y_coor):
        if x_coor == 0: # top row
            if len(matrix) == 1: # matrix is a single row
                if y_coor == 0: # left col
                    if len(matrix[0]) == 1: # matrix is a single col
                        return -1
                    else:
                        if matrix[x_coor][y_coor + 1] > 0:
                            to_convert_array.append((x_coor, y_coor))
                elif 0 < y_coor < len(matrix[0]) - 1: # mid col
                    if matrix[x_coor][y_coor - 1] > 0 or matrix[x_coor][y_coor + 1] > 0:
                        to_convert_array.append((x_coor, y_coor))
                elif y_coor == len(matrix[0]) - 1: # right col
                    if matrix[x_coor][y_coor - 1] > 0:
                        to_convert_array.append((x_coor, y_coor))

            else: # matrix not a single row
                if y_coor == 0:  # left col
                    if len(matrix[0]) == 1:  # matrix is a single col
                        if matrix[x_coor + 1][y_coor] > 0:
                            to_convert_array.append((x_coor, y_coor))
                    else:
                        if matrix[x_coor + 1][y_coor] > 0 or matrix[x_coor][y_coor + 1] > 0:
                            to_convert_array.append((x_coor, y_coor))
                elif 0 < y_coor < len(matrix[0]) - 1: # mid col
                    if matrix[x_coor + 1][y_coor] > 0 or matrix[x_coor][y_coor + 1] > 0 or matrix[x_coor][y_coor - 1] > 0:
                        to_convert_array.append((x_coor, y_coor))
                elif y_coor == len(matrix[0]) - 1:  # right col
                    if matrix[x_coor + 1][y_coor] > 0 or matrix[x_coor][y_coor - 1] > 0:
                        to_convert_array.append((x_coor, y_coor))

        elif 0 < x_coor < len(matrix) - 1: # mid row
            if y_coor == 0: # left col
                if len(matrix[0]) == 1: # matrix is a single col
                    if matrix[x_coor - 1][y_coor] > 0 or matrix[x_coor + 1][y_coor] > 0:
                        to_convert_array.append((x_coor, y_coor))
                else: # matrix not a single col
                    if matrix[x_coor - 1][y_coor] > 0 or matrix[x_coor + 1][y_coor] > 0 or matrix[x_coor][y_coor + 1] > 0:
                        to_convert_array.append((x_coor, y_coor))
            elif 0 < y_coor < len(matrix[0]) - 1: # mid col
                if matrix[x_coor - 1][y_coor] > 0 or matrix[x_coor + 1][y_coor] > 0 or matrix[x_coor][y_coor - 1] > 0 or matrix[x_coor][y_coor + 1] > 0:
                    to_convert_array.append((x_coor, y_coor))
            elif y_coor == len(matrix[0]) - 1: # right col
                if matrix[x_coor - 1][y_coor] > 0 or matrix[x_coor + 1][y_coor] > 0 or matrix[x_coor][y_coor - 1] > 0:
                    to_convert_array.append((x_coor, y_coor))

        elif x_coor == len(matrix) - 1: # bottom row
            if y_coor == 0: # left col
                if len(matrix[0]) == 1:  # matrix is a single col
                    if matrix[x_coor - 1][y_coor] > 0:
                        to_convert_array.append((x_coor, y_coor))
                else:
                    if matrix[x_coor - 1][y_coor] > 0 or matrix[x_coor][y_coor + 1] > 0:
                        to_convert_array.append((x_coor, y_coor))
            elif 0 < y_coor < len(matrix[0]) - 1: # mid col
                if matrix[x_coor - 1][y_coor] > 0 or matrix[x_coor][y_coor - 1] > 0 or matrix[x_coor][y_coor + 1] > 0:
                    to_convert_array.append((x_coor, y_coor))
            elif y_coor == len(matrix[0]) - 1: # right col
                if matrix[x_coor - 1][y_coor] > 0 or matrix[x_coor][y_coor - 1] > 0:
                    to_convert_array.append((x_coor, y_coor))

    def numConverter(coor_array):
        for coor in coor_array:
            x_coor = coor[0]
            y_coor = coor[1]

            matrix[x_coor][y_coor] *= -1

    number_of_passes = 0
    matrix_has_changed = True
    while matrix_has_changed:
        to_convert_array = []
        x_coor = 0
        y_coor = 0
    
        # looping through the whole matrix
        while x_coor < len(matrix):
            while y_coor < len(matrix[0]):
                current_num = matrix[x_coor][y_coor]
                if current_num < 0:
                    checkAdjacentNum(x_coor, y_coor)

                y_coor += 1

            y_coor = 0
            x_coor += 1

        if len(to_convert_array) == 0:
            matrix_has_changed = False
        else:
            numConverter(to_convert_array)
            number_of_passes += 1

    all_numbers_are_positives = True
    x_coor = 0
    y_coor = 0
    while x_coor < len(matrix) and all_numbers_are_positives:
        while y_coor < len(matrix[0]):
            current_num = matrix[x_coor][y_coor]
            if current_num < 0:
                all_numbers_are_positives = False
                break
            y_coor += 1
        
        x_coor += 1
        y_coor = 0

    if all_numbers_are_positives:
        return number_of_passes
    else:
        return -1

# brute force method, passing multiple times through the same coordinates (could be avoided)
# finding negative numbers, then checking adjacent numbers for a positive number
# if a positive one is found, then coordinates are recorded to be converted later
# once no more numbers can be converted, checks if the matrix contains negative numbers
# if it does then returns -1, else returns the number of passes

# [0, -2, -1]
# [-5, 2, 0]
# [-6, -2, 0]