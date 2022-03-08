# https://www.algoexpert.io/questions/Validate%20Subsequence

# first version
def isValidSubsequence(array, sequence):
	if len(sequence) > len(array):
		return False

	currentIndex = 0
	for n in sequence:
		if n not in array[currentIndex:]:
			return False
		currentIndex += array[currentIndex:].index(n) + 1

	return True

# first if statement clears out easily identifiable False cases
# += for the current index and not = because we are moving in the original array 
# and not just the sliced array
# + 1 because we start at index 0, so we need to move the current index 
# one index to the right

# Poor time complexity

# notes
# "array": [5, 1, 22, 25, 6, -1, 8, 10],
# "sequence": [1, 6, -1, 10], 1, 4, 5, 7 
# 0 1 3 2

# print(f"idx : {currentIndex}")
# print(f"n : {n}")
# print(array[currentIndex:])