# https://www.algoexpert.io/questions/Nth%20Fibonacci

# Fn is the nth number of fibonacci
# For this problem we are going to use n = 1 returns F0, n = 2 returns F1...

# First solution

# Fn // 0, 1, 1, 2, 3, 5...
# n // 1, 2, 3, 4, 5, 6...
def getNthFib(n):
    fibonacci_list = []
    for i in range(0, n):
        if i == 0:
            fibonacci_number = 0
        elif i == 1:
            fibonacci_number = 1
        else:
            fibonacci_number = fibonacci_list[i-2] + fibonacci_list[i-1]
        fibonacci_list.append(fibonacci_number)
    fibonacci_list.reverse()
    return fibonacci_list[0]

# O(n)T, O(n)S
# Can try to optimize the space, only the 2 previous fibonacci are necessary to find the next one

# Second solution

def getNthFib(n):
    fibonacci_list = []
    for i in range(0, n):
        if i == 0:
            fibonacci_number = 0
        elif i == 1:
            fibonacci_number = 1
        else:
            fibonacci_number = fibonacci_list[0] + fibonacci_list[1]
            fibonacci_list.pop(0)
        fibonacci_list.append(fibonacci_number)

    fibonacci_list.reverse()
    return fibonacci_list[0]

# O(n)T, O(1)S
# len(fibonacci_list) <= 2