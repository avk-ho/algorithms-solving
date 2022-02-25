# https://www.algoexpert.io/questions/Binary%20Search

# First attempt
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1