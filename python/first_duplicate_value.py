# https://www.algoexpert.io/questions/First%20Duplicate%20Value

# First solution
def firstDuplicateValue(array):
    memory = []
    for i in array:
        if i in memory:
            return i
        else:
            memory.append(i)
    return -1

# O(n) ST