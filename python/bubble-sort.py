# https://www.algoexpert.io/questions/Bubble%20Sort

# First solution
def bubbleSort(array):
    did_swap = True
    while did_swap:
        did_swap = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                did_swap = True
    return array

# Second solution
def bubbleSort(array):
    did_swap = True
    counter = len(array) - 1
    while did_swap:
        did_swap = False
        for i in range(counter):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                did_swap = True
        counter -= 1
    return array