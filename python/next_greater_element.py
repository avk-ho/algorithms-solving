# https://www.algoexpert.io/questions/Next%20Greater%20Element

# output[i] should be the next (order) greater element of array[i], or -1 if there isn't
# array should be treated as circular

# First attempt

def nextGreaterElement(array):
    output = []
    for i in range(len(array)):
        if array[i] == max(array):
            output.append(-1)
        else:
            start = i
            array_from_start = [
                array[(start + h) % len(array)] for h in range(len(array))]

            for elem in array_from_start[1::]:
                if elem > array[i]:
                    output.append(elem)
                    break

    return output

# Brute force method, nested loop
# Poor time complexity O(n²) T

# [2, 5, -3, -4, 6, 7, 2] input
# [5, 6, 6, 6, 7, -1, 5] output
# -4:3, -3:2, 2:[0, 6], 5:1, 6:4, 7:5


# Second solution
# Using stack
def nextGreaterElement(array):
    output = [-1 for _ in range(len(array))]
    stack = []

    for n in range(2 * len(array)):
        idx = n % len(array)
        current_elem = array[idx]
        
        if len(stack) > 0:
            stack_top = stack[len(stack) - 1]

        while len(stack) > 0 and array[stack_top] < current_elem:
            stack_top = stack.pop()
            output[stack_top] = current_elem
            if len(stack) > 0:
                stack_top = stack[len(stack) - 1]

        stack.append(idx)

    return output

# Linear space time complexity, O(n)ST


# Experimental attempt (non functional)
# def nextGreaterElement(array):

#     idx_dict = {}
#     for i in range(len(array)):
#         if array[i] not in idx_dict:
#             idx_dict[array[i]] = i
#         elif type(idx_dict[array[i]]) == list:
#             idx_dict[array[i]].append(i)
#         else:
#             idx_dict[array[i]] = [idx_dict[array[i]], i]

#     sorted_array = array
#     sorted_array.sort()
#     for elem in sorted_array:
#         while sorted_array.count(elem) > 1:
#             sorted_array.remove(elem)

#     output = []
#     for i in range(len(array)):
#         if array[i] == max(array):
#             output.append(-1)
#         else:
#             idx = sorted_array.index(array[i])
#             greater_idx_list = []
#             for elem in sorted_array[idx::]:
#                 if type(idx_dict[elem]) == list:
#                     greater_idx_list.extend(idx_dict[elem])
#                 else:
#                     greater_idx_list.append(idx_dict[elem])
#             greater_idx_list.sort()
#             idx_in_greater = greater_idx_list.index(idx)
#             if idx_in_greater == len(greater_idx_list) - 1:
#                 output.append(greater_idx_list[0])
#             else:
#                 output.append(greater_idx_list[idx_in_greater + 1])
            
#     return output
