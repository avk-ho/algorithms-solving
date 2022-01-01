# https://www.algoexpert.io/questions/Non-Constructible%20Change

# coins is an array of positive integers

# First version
def nonConstructibleChange(coins):
    if coins:
        coins.sort()
        coins.reverse()
        i = 1

        change_possible = True
        while change_possible:
            #print(f"i = {i}")
            remainder = i
            coins_copy = coins.copy()
            for j in range(0, len(coins)):
                coin = coins[j]
                #print(f"remainder = {remainder}")
                if remainder in coins_copy:
                    i += 1
                    break
                if (remainder - coin) > 0:
                    remainder = remainder - coin
                    coins_copy.remove(coin)

                if j == len(coins) - 1:
                    change_possible = False

        return i


    else:
        return 1

#x = [5, 7, 1, 1, 2, 3, 22] # expected result 20
#y = nonConstructibleChange(x)

