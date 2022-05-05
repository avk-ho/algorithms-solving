# https://www.algoexpert.io/questions/Task%20Assignment

# First solution
def taskAssignment(k, tasks):
    assignment = []
    tasks_copy = tasks.copy()

    while k > 0:
        longest_task = max(tasks_copy)
        shortest_task = min(tasks_copy)
        longest_task_index = tasks.index(longest_task)
        shortest_task_index = tasks.index(shortest_task)

        pair = [longest_task_index, shortest_task_index]
        assignment.append(pair)

        tasks[longest_task_index], tasks[shortest_task_index] = "x", "x"

        tasks_copy.remove(longest_task)
        tasks_copy.remove(shortest_task)

        k -= 1

    return assignment

# can't sort tasks because we need the original indexes
# k = 3 // tasks = [1, 3, 5, 3, 1, 4]
# k = 1 // tasks = [1, 7]
# k = 2 // tasks = [1, 7, 5, 5]
# k = 2 // tasks = [1, 5, 7, 8]
# k = 3 // tasks = [1, 2, 6, 6, 8, 7]

# Second solution
def taskAssignment(k, tasks):
    assignment = []
    sorted_tasks = sorted(tasks)
    
    while k > 0:
        longest_task = sorted_tasks[len(sorted_tasks) - 1]
        shortest_task = sorted_tasks[0]
        longest_task_index = tasks.index(longest_task)
        shortest_task_index = tasks.index(shortest_task)

        pair = [longest_task_index, shortest_task_index]
        assignment.append(pair)

        tasks[longest_task_index], tasks[shortest_task_index] = "x", "x"

        sorted_tasks.pop(0)
        sorted_tasks.pop()

        k -= 1

    return assignment

