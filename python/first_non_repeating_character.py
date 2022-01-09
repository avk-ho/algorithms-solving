# https://www.algoexpert.io/questions/First%20Non-Repeating%20Character

# First solution
def firstNonRepeatingCharacter(string):
    input = list(string)
    for chr in input:
        if input.count(chr) == 1:
            return input.index(chr)
    return -1