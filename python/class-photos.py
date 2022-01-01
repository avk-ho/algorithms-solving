# https://www.algoexpert.io/questions/Class%20Photos

# 2 arrays of int as inputs

# First solution
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    max_red = max(redShirtHeights)
    max_blue = max(blueShirtHeights)
    if max_red == max_blue:
        return False
    elif max_red > max_blue:
        for i in range(0, len(redShirtHeights)):
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
    else:
        for i in range(0, len(redShirtHeights)):
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
    return True