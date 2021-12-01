# https://www.algoexpert.io/questions/Sorted%20Squared%20Array

# first version

def sortedSquaredArray(array):
	result = []
    for element in array:
		result.append(element*element)
	result.sort()
    return result