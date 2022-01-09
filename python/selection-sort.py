# https://www.algoexpert.io/questions/Selection%20Sort

# First solution
def selectionSort(array):
    def swap(i, j, array):
        array[i], array[j] = array[j], array[i]

    counter = 0
    while counter < len(array) - 1:
        smallest_index = counter
        for i in range(counter + 1, len(array)):
            if array[i] < array[smallest_index]:
                smallest_index = i
        swap(counter, smallest_index, array)
        counter += 1

    return array