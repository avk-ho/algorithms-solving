# https://www.algoexpert.io/questions/Single%20Cycle%20Check

# First solution
def hasSingleCycle(array):
    memory = []
    j = 0
    for i in range(len(array)):
        if j < 0 or j >= len(array):
            j = j % len(array)
        memory.append(array[j])
        j += array[j]

    array.sort()
    memory.sort()
    single_cycle = array == memory

    return single_cycle

# Imperfect solution

# With hints
# At n+1 with n = len(array), we should be back at the start of the array (array[0])
# If at any point before we get through the entire array we get again the starting index (0)
# then it isn't a single cycle

def hasSingleCycle(array):
    j = 0
    for i in range(len(array)):
        if i > 0 and j == 0: # if we get back to the index 0 after the start (before the loop ends), then it isn't a single cycle
            return False
        if j < 0 or j >= len(array): # handles the cases where the index j jump past the bound of the array
            j = j % len(array)
        j += array[j]

    if j % len(array) == 0: # checks if we are back at the index 0 of the array
        return True
    else:
        return False
