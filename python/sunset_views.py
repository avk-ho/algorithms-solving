# https://www.algoexpert.io/questions/Sunset%20Views

# First attempt
# output must be sorted in ascending order

def sunsetViews(buildings, direction):
    output = []

    # Direction is "EAST"
    if direction == "EAST":
        current_tallest = 0
        left_pointer = 0
        while left_pointer <= len(buildings) - 1:
            current_tallest = buildings.index(max(buildings))
            buildings[current_tallest] *= -1

            if current_tallest >= left_pointer:
                left_pointer = current_tallest + 1
                while buildings[current_tallest] * -1 in buildings:
                    current_tallest = buildings.index(max(buildings))
                    left_pointer = current_tallest + 1
                    buildings[current_tallest] *= -1

                output.append(current_tallest)

    # Direction is "WEST"
    if direction == "WEST":
        current_tallest = 0
        right_pointer = len(buildings) - 1
        while right_pointer >= 0:
            current_tallest = buildings.index(max(buildings))
            buildings[current_tallest] *= -1

            if current_tallest <= right_pointer:
                right_pointer = current_tallest - 1
                output.append(current_tallest)

    output.sort()

    return output

# Possibility to remove the nested while loop in the east direction part to explore

# Notes
# 3 5 4 4 3 1 3 2 // 1 3 6 7, lp0, len-1 == 7
# 3 -5 4 4 3 1 3 2 // 1, lp 2
# 3 -5 -4 4 3 1 3 2 // 1, lp 3
# 3 -5 -4 -4 3 1 3 2 // 1, 3, lp 4

# 3 5 4 4 3 1 3 2 // 0 1, rp7, len-1 == 7
# 3 -5 4 4 3 1 3 2 // 1, rp0
# 3 -5 -4 4 3 1 3 2 // 1, rp0
# 3 -5 -4 -4 3 1 3 2 // 1, rp0
# -3 -5 -4 -4 3 1 3 2 // 1 0, rp-1