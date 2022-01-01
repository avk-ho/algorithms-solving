# https://www.algoexpert.io/questions/Tandem%20Bicycle

# 2 arrays of int and a boolean as inputs

# First solution
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if fastest:
        max_speed = 0
        red_copy = redShirtSpeeds.copy()
        blue_copy = blueShirtSpeeds.copy()
        for i in range(0, len(redShirtSpeeds)):
            max_red = max(red_copy)
            max_blue = max(blue_copy)
            if max_red >= max_blue:
                min_blue = min(blue_copy)
                
                red_copy.remove(max_red)
                blue_copy.remove(min_blue)

                max_speed += max_red
            else:
                min_red = min(red_copy)

                red_copy.remove(min_red)
                blue_copy.remove(max_blue)

                max_speed += max_blue
        return max_speed

    else:
        min_speed = 0
        for i in range(0, len(redShirtSpeeds)):
            pair = [redShirtSpeeds[i], blueShirtSpeeds[i]]
            min_speed += max(pair)
        return min_speed