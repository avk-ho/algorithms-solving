# https://www.algoexpert.io/questions/Longest%20Peak

# First solution
# A peak is at least 2 consecutive strictly increasing numbers 
# followed by at least 1 decreasing number.
# [1, 3, 2]
def longestPeak(array):
    longest_peak = 0
    ascending_streak = 0
    descending_streak = 0
    current_peak = 0
    if len(array) < 3: # no peak possible
        return longest_peak
    else:
        for i in range(1, len(array)):
            if array[i-1] < array[i] and descending_streak > 0: # starting a new peak and saving the previous one if needed
                if current_peak > longest_peak:
                    longest_peak = current_peak
                ascending_streak = 2
                descending_streak = 0
            elif array[i-1] < array[i] and descending_streak == 0: # starting a new peak
                if ascending_streak == 0:
                    ascending_streak = 2
                else:
                    ascending_streak += 1
            elif array[i-1] > array[i] and ascending_streak > 0: # only counting after a peak
                descending_streak += 1
            else: # array[i] == array[i+1] // a plateau, ending any eventual peak and resetting the processus
                if current_peak > longest_peak:
                    longest_peak = current_peak
                ascending_streak = 0
                descending_streak = 0
            if ascending_streak != 0 and descending_streak != 0 and ascending_streak + descending_streak >= 3: # updating the length of the current peak
                current_peak = ascending_streak + descending_streak
            #print(f"current peak : {current_peak} / asc : {ascending_streak} / desc : {descending_streak}")
        if current_peak > longest_peak: # in case the current peak when the end of the array is reached is the longest
            longest_peak = current_peak
        return longest_peak

# Possibility to slightly reduce the O()T by mesuring the length of the current
# longest peak and comparing it to the remaining length of the array

# Second solution
def longestPeak(array):
    longest_peak = 0
    ascending_streak = 0
    descending_streak = 0
    current_peak = 0
    if len(array) < 3:
        return longest_peak
    else:
        for i in range(1, len(array)):
            if array[i-1] < array[i] and descending_streak > 0:
                if current_peak > longest_peak:
                    longest_peak = current_peak
                ascending_streak = 2
                descending_streak = 0
            elif array[i-1] < array[i] and descending_streak == 0:
                if ascending_streak == 0:
                    ascending_streak = 2
                else:
                    ascending_streak += 1
            elif array[i-1] > array[i] and ascending_streak > 0:
                descending_streak += 1
            else: # array[i] == array[i+1]
                if current_peak > longest_peak:
                    longest_peak = current_peak
                ascending_streak = 0
                descending_streak = 0
            if ascending_streak != 0 and descending_streak != 0 and ascending_streak + descending_streak >= 3:
                current_peak = ascending_streak + descending_streak
            if longest_peak >= len(array)-i: # if a longer peak can no longer be created, end the loop early
                break
            print(f"longest : {longest_peak} / current : {current_peak} / asc : {ascending_streak} / desc : {descending_streak}")
        if current_peak > longest_peak:
            longest_peak = current_peak
        return longest_peak