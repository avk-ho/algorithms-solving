# https://www.algoexpert.io/questions/Two%20Number%20Sum

# first version
# not using python ability to search efficiently here
# resulting in loops iterating through the whole array
# added a quick end if a pair is found
def twoNumberSum(array, targetSum):
	output = []
	array_copy = array.copy()
	for element in array:
		array_copy.remove(element)
		for element2 in array_copy:
			#print(f"{element} - {element2}")
			if element + element2 == targetSum:
				output.append(element)
				output.append(element2)
			if len(output) > 0: # end the function early if pair is found
				break
		if len(output) > 0: #end the function early if a pair is found
				break
	return output