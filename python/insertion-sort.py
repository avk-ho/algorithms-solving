# https://www.algoexpert.io/questions/Insertion%20Sort

# First solution
def insertionSort(array):
    def swap(n):
        if n >= 0:
            if array[n] > array[n+1]:
                temp = array[n+1]
                array[n+1] = array[n]
                array[n] = temp
            swap(n-1)
    
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            swap(i)
    return array
