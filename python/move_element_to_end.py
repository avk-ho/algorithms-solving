# https://www.algoexpert.io/questions/Move%20Element%20To%20End

# First solution
def moveElementToEnd(array, toMove):
    def swap(i, j, array):
        array[i], array[j] = array[j], array[i]

    toMove_count = array.count(toMove)
    index = 0
    end_index = -1 # equivalent to len(array) - 1
    while toMove_count != 0:
        if array[end_index] == toMove:
            end_index -= 1
            toMove_count -= 1
        else:
            if array[index] == toMove:
                swap(index, end_index, array)
            else:
                index += 1

    return array

# [2, 1, 2, 2, 2, 3, 4, 2]

# Second solution
def moveElementToEnd(array, toMove):
    def swap(i, j, array):
        array[i], array[j] = array[j], array[i]

    toMove_count = array.count(toMove)
    index = 0
    end_index = -1 # equivalent to len(array) - 1
    while toMove_count != 0:
        if array[end_index] == toMove:
            end_index -= 1
            toMove_count -= 1
        else:
            while array[index] != toMove:
                index += 1
            swap(index, end_index, array)

    return array