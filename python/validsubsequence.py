# https://www.algoexpert.io/questions/Validate%20Subsequence

# first version
# wanted to make use of item in list but ended up being a stuck
# first if statement clears out easily identifiable False cases

def isValidSubsequence(array, sequence):
	if len(sequence) > len(array):
		return False
    sequenceIndex = 0
	for element in array:
		if element == sequence[sequenceIndex]:
			sequenceIndex += 1
		if sequenceIndex == len(sequence):
			return True
	return False