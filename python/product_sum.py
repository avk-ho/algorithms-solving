# https://www.algoexpert.io/questions/Product%20Sum

# First attempt
def productSum(array):
    result = 0
    for n in array:
        if type(n) == list:
            n = productSumHelper(n)
        result += n

    return result

def productSumHelper(array, depth=2):
    result = 0
    for n in array:
        if type(n) == list:
            n = productSumHelper(n, depth + 1)
        result += n
    return result * depth

# [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


# Second attempt
# If modifying the original function is possible
def productSumTwo(array, depth=1):
    result = 0
    for n in array:
        if type(n) == list:
            n = productSumTwo(n, depth + 1)
        result += n
    return result * depth
