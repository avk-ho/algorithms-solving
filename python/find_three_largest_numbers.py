# https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers

# No sorting of the input array allowed
# Also returns multiple duplicates if necessary

# First solution
def findThreeLargestNumbers(array):
    def sort(array):
        for i in range(0, 2):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
            if i > 0:
                if array[i] < array[i-1]:
                    temp2 = array[i-1]
                    array[i-1] = array[i]
                    array[i] = temp2

    solution_array = []

    counter = 0
    for number in array:
        if counter < 3:
            solution_array.append(number)
        else:
            if number > solution_array[0]:
                solution_array[0] = number
        if counter >= 2:
            sort(solution_array)
        #print(solution_array)
        counter += 1

    return solution_array

# Second solution
# Same solution, without using a counter
def findThreeLargestNumbers(array):
    def sort(array):
        for i in range(0, 2):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
            if i > 0:
                if array[i] < array[i-1]:
                    temp2 = array[i-1]
                    array[i-1] = array[i]
                    array[i] = temp2

    solution_array = []

    for number in array:
        if len(solution_array) < 3:
            solution_array.append(number)
        else:
            if number > solution_array[0]:
                solution_array[0] = number
        if len(solution_array) >= 2:
            sort(solution_array)
        #print(solution_array)

    return solution_array