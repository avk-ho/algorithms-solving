# https://www.algoexpert.io/questions/Three%20Number%20Sum

# First attempt
def threeNumberSum(array, targetSum):
    array.sort()
    output = []

    for i in range(len(array)-2):
        target = targetSum - array[i]

        if i+1 == len(array)-2:
            target_two = target - array[i+1] - array[i+2]
            if target_two == 0:
                trio = []
                trio.append(array[i])
                trio.append(array[i+1])
                trio.append(array[i+2])
                output.append(trio)
            else:
                continue
        else:
            for j in range(i+1, len(array)-2):
                target_two = target - array[j]

                if target_two in array[j+1:]:
                    trio = []
                    trio.append(array[i])
                    trio.append(array[j])
                    trio.append(target_two)
                    output.append(trio)
                else:
                    continue

    return output

# Correction solution
def threeNumberSum(array, targetSum):
    array.sort()
    output = []

    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                output.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum > targetSum:
                right -= 1
            elif currentSum < targetSum:
                left += 1

    return output


# "targetSum": 0
# "array": [12, 3, 1, 2, -6, 5, -8, 6]
# sorted : [-8, -6, 1, 2, 3, 5, 6, 12]
# i = 0 // target = 8 -> target = 14

# array: [1, 2, 3]
# i = 0 // 

