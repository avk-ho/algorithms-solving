# https://www.algoexpert.io/questions/Spiral%20Traverse

# First solution
def spiralTraverse(array):
    output = []
    # x is the horizontal plane, y is the vertical plane
    # x is the column, y is the row 
    max_y = len(array) - 1
    max_x = len(array[0]) - 1
    min_x = 0
    min_y = 0
    while min_x <= max_x and min_y <= max_y:
        if min_x >= max_x:
            for y in range(min_y, max_y+1):
                output.append(array[y][min_x])
                print(output)
            return output
        elif min_y >= max_y:
            for x in range(min_x, max_x+1):
                output.append(array[min_y][x])
                print(output)
            return output
        else:
            for x in range(min_x, max_x+1):
                output.append(array[min_y][x])
                print(output)
            min_y += 1
            for y in range(min_y, max_y+1):
                output.append(array[y][max_x])
                print(output)
            max_x -= 1
            x = max_x
            while x >= min_x:
                output.append(array[max_y][x])
                print(output)
                x -= 1
            max_y -= 1
            y = max_y
            while y >= min_y:
                output.append(array[y][min_x])
                print(output)
                y -= 1
            min_x += 1
    return output

# [1 2 3] - [0 1] - [0 1 2] - [0 1]
# [8 9 4] - [0 1] - [0 1 2] - [0 1]
# [7 6 5] - [0 1] - - - - - - 

# [0] - [0 1]
# [0] - - - -
# Second solution
# Switched the inner while loops for reversed range for loops
def spiralTraverse(array):
    output = []
    # x is the horizontal plane, y is the vertical plane
    # x is the column, y is the row 
    max_y = len(array) - 1
    max_x = len(array[0]) - 1
    min_x = 0
    min_y = 0
    while min_x <= max_x and min_y <= max_y:
        if min_x >= max_x:
            for y in range(min_y, max_y+1):
                output.append(array[y][min_x])
                print(output)
            return output
        elif min_y >= max_y:
            for x in range(min_x, max_x+1):
                output.append(array[min_y][x])
                print(output)
            return output
        else:
            for x in range(min_x, max_x+1):
                output.append(array[min_y][x])
                print(output)
            min_y += 1
            for y in range(min_y, max_y+1):
                output.append(array[y][max_x])
                print(output)
            max_x -= 1
            for x in reversed(range(min_x, max_x+1)):
                output.append(array[max_y][x])
                print(output)
            max_y -= 1
            for y in reversed(range(min_y, max_y+1)):
                output.append(array[y][min_x])
                print(output)
            min_x += 1
    return output