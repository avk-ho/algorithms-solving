# https://www.algoexpert.io/questions/Array%20Of%20Products

# Rule : cannot use division to solve the problem and no mutation of the input array
# First solution
def arrayOfProducts(array):
    result = []
    for i in range(len(array)):
        result[i] = 1
        for j in range(len(array)):
            if j != i:
                result[i] *= array[j]
        
    return result

# Brute force method : a loop within another loop, not great
# O(n²)T O(n)S

# [1, 2, 3] | [3, 2, 1] // [6, 3, 2] // [0, 1, 2] | [-3, -2, -1]
# [5, 1, 4, 2] | [2, 4, 1, 5] // [8, 40, 10, 20] // [0, 1, 2, 3] | [-4, -3, -2, -1]
