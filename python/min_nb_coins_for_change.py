# https://www.algoexpert.io/questions/Min%20Number%20Of%20Coins%20For%20Change

# First solution
def minNumberOfCoinsForChange(n, denoms):
    denoms.sort()
    denoms.reverse()
    nb_coins = 0
    remainder = 0
    for coin in denoms:
        if coin > n:
            continue
        print(f"n = {n} // coin = {coin}")
        while n >= coin:
            n = n - coin
            nb_coins += 1
    if n != 0:
        return -1
    else:
        return nb_coins

# Imperfect solution

# With 1st hint
def minNumberOfCoinsForChange(n, denoms):
    def n_reduction(remainder, j, nb_coins, denoms):
        coin = denoms[j]
        while remainder >= coin:
            remainder -= coin
            nb_coins += 1
        print(f"remainder = {remainder} // coin = {coin} // nb coins = {nb_coins}")
        if remainder == 0:
            return nb_coins
        elif remainder > 0 and j != 0:
            return n_reduction(remainder, j-1, nb_coins, denoms)
        elif remainder > 0 and j == 0:
            return -1
    
    if n == 0:
        return 0

    denoms.sort()
    min_nb_coins = []

    for i in range(len(denoms)):
        coin = denoms[i]
        if coin > n:
            break

        nb_coins = 0
        remainder = n
        min_nb = n_reduction(remainder, i, nb_coins, denoms)
        if min_nb < 0:
            continue
        else:
            min_nb_coins.append(min_nb)

    if len(min_nb_coins) == 0:
        return -1
    else:
        result = min(min_nb_coins)
        return result

# 1 miss [1, 3, 4] // n = 10, returns 4 (4x2, 1x2), answer 3 (3x2 + 4x1)

# 3rd attempt
# Added early end in n_reduction function, fixes the previous miss
def minNumberOfCoinsForChange(n, denoms):
    def n_reduction(remainder, j, nb_coins, denoms):
        coin = denoms[j]
        while remainder >= coin:
            # this condition allows to check if we can use bigger denom to end the function
            # also makes the answer more accurate
            if remainder in denoms:
                nb_coins += 1
                remainder = 0
                return nb_coins
            else:
                remainder -= coin
                nb_coins += 1
        print(f"remainder = {remainder} // coin = {coin} // nb coins = {nb_coins}")
        if remainder == 0:
            return nb_coins
        elif remainder > 0 and j != 0:
            return n_reduction(remainder, j-1, nb_coins, denoms)
        elif remainder > 0 and j == 0:
            return -1
    
    if n == 0:
        return 0

    denoms.sort()
    min_nb_coins = []

    for i in range(len(denoms)):
        coin = denoms[i]
        if coin > n:
            break

        nb_coins = 0
        remainder = n
        min_nb = n_reduction(remainder, i, nb_coins, denoms)
        if min_nb < 0:
            continue
        else:
            min_nb_coins.append(min_nb)

    if len(min_nb_coins) == 0:
        return -1
    else:
        result = min(min_nb_coins)
        return result