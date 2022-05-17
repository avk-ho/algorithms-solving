# https://www.algoexpert.io/questions/Merge%20Overlapping%20Intervals

# Fist solution
def mergeOverlappingIntervals(intervals):
    intervals.sort()
    output = []

    currentInterval = []
    for interval in intervals:
        if len(currentInterval) == 0:
            currentInterval = interval
        else:
            currentIntervalEnd = currentInterval[1]
            newIntervalStart = interval[0]
            newIntervalEnd = interval[1]
            if currentIntervalEnd < newIntervalStart:
                output.append(currentInterval)
                currentInterval = interval
            elif currentIntervalEnd < newIntervalEnd:
                currentInterval[1] = interval[1]
    
    output.append(currentInterval)

    return output

# O(nlog(n)) T # because of the sorting
# O(n) S
# intervals is always non-empty in this problem, 
# solution would have to be diffrent to handle potential empty intervals

# input [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
# output [[1, 2], [3, 8], [9, 10]]
# [1, 22], [-20, 30]
# [-20, 30]