# https://www.algoexpert.io/questions/Three%20Number%20Sort

# array must be mutated 
# array may not contain all the integers in order
# order is always 3 int

# First solution

def threeNumberSort(array, order):
    left = 0

    for elem in order:
        right = len(array) - 1

        while left <= right:
            print(
                f"array: {array} // left:{array[left]} // right: {array[right]}")
            if array[left] == elem:
                left += 1
            else:
                if array[right] == elem:
                    array[left], array[right] = array[right], array[left]
                    left += 1

                right -= 1
            

    return array

# this solution does not take into account that order is always 3 int

# array = [1, 0, 0, -1, -1, 0, 1, 1]
# order = [0, 1, -1]