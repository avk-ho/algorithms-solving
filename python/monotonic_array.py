# https://www.algoexpert.io/questions/Monotonic%20Array

# First solution
def isMonotonic(array):
    is_monotonic = True
    trend = ""
    for i in range(1, len(array)):
        difference = array[i-1] - array[i]
        if trend == "":
            if difference < 0:
                trend = "dec"
            elif difference > 0:
                trend = "inc"
        if difference < 0 and trend == "inc":
            is_monotonic = False
            return is_monotonic
        elif difference > 0 and trend == "dec":
            is_monotonic = False
            return is_monotonic
    return is_monotonic

# More elegant solution (correction)
def isMonotonic(array):
    is_entirely_increasing = True
    is_entirely_decreasing = True
    for i in range(1, len(array)):
        difference = array[i-1] - array[i]
        if difference < 0:
            is_entirely_increasing = False
        elif difference > 0:
            is_entirely_decreasing = False
        
    return is_entirely_increasing or is_entirely_decreasing