# https://www.algoexpert.io/questions/Minimum%20Waiting%20Time

# time until the last query is initiated

# First attempt
def minimumWaitingTime(queries):
    queries.sort(reverse=True)
    waiting_time = 0
    query_wait = 0
    while len(queries) > 1:
        query = queries.pop()
        query_wait += query
        waiting_time += query_wait
    return waiting_time

# [3, 2, 1, 2, 6] // 17
# 0, 3, 5, 6, 8

# [1, 2, 2, 3, 6]
# 0, 1, 3, 5, 8