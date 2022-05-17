# https://www.algoexpert.io/questions/Powerset

# First solution
def powerset(array):
    output = [[]]

    for i in range(len(array)):
        temp_output = []
        for subset in output:
            subset_copy = subset.copy()
            subset_copy.append(array[i])
            temp_output.append(subset_copy)
        output.extend(temp_output)

    return output

# O(n*2^n) ST

# Cleaner version
def powerset(array):
    output = [[]]

    for elem in array:
        for i in range(len(output)):
            currentSubset = output[i]
            output.append(currentSubset + [elem])

    return output

# notes
# space complexity of the output == 2^n ?
# [1, 2, 3]
# [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
# [1, 2]
# [[], [1], [2], [1, 2]]
# [1, 2, 3, 4]
# [[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4],
# [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]