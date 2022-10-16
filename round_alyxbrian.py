import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def round_alyxbrian(n,decimals):
    numb = n
    n_decimals = len(str(numb).split(".")[1])
    if n_decimals<= decimals:
        return numb
    else:
        for i in reversed(range(1,n_decimals+1)):
            numb = round_half_up(numb,i-1)
            if i-1 == decimals:
                return numb
