# https://www.algoexpert.io/questions/Permutations

# First solution
def getPermutations(array):

    def getPermutationsHelper(output_array):
        # if the array in input is complete, appends to the output array and stops
        if len(output_array) == len(array):
            permutations_list.append(output_array)
        else:
            # recursive call for each remaining possible element of array at the next position
            # possible because every element is unique/distinct
            for elem in array:
                if elem in output_array:
                    continue
                else:
                    new_output = output_array.copy()
                    new_output.append(elem)
                    getPermutationsHelper(new_output)

    permutations_list = []

    for elem in array:
        permutation = [elem]
        getPermutationsHelper(permutation)

    return permutations_list

# O(n*n!) S / O(n!*n²) T (upper bound)
# Time complexity can be improved by swapping elements 
# instead of creating a new array

# [1, 2, 3]
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# [1, 2, 3, 4]
# [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2]
