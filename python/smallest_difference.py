# https://www.algoexpert.io/questions/Smallest%20Difference

# First solution
def smallestDifference(arrayOne, arrayTwo):
    smallest_pair = []
    arrayOne.sort()
    arrayTwo.sort()
    for i in range(len(arrayOne)):
        nb1 = arrayOne[i]
        for j in range(len(arrayTwo)):
            nb2 = arrayTwo[j]
            if i == 0 and j == 0:
                if nb1 > nb2:
                    smallest_difference = abs(nb1 - nb2)
                    smallest_pair.append(nb1)
                    smallest_pair.append(nb2)
                else:
                    smallest_difference = abs(nb2 - nb1)
                    smallest_pair.append(nb1)
                    smallest_pair.append(nb2)

            elif nb1 > nb2:
                if smallest_difference > abs(nb1 - nb2):
                    smallest_difference = abs(nb1 - nb2)
                    smallest_pair[0] = nb1
                    smallest_pair[1] = nb2
            
            elif nb2 > nb1:
                if smallest_difference > abs(nb2 - nb1):
                    smallest_difference = abs(nb2 - nb1)
                    smallest_pair[0] = nb1
                    smallest_pair[1] = nb2
            else:
                smallest_pair[0] = nb1
                smallest_pair[1] = nb2
                return smallest_pair
    
    return smallest_pair

# Fairly brute force solution
# The better solution increment each array separately 
# depending on the result of the previous difference