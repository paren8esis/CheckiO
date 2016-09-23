from math import floor, factorial

def binom(x, y):
    '''
    Computes the binomial coefficient of x, y
    '''
    return factorial(x)/(factorial(x-y)*factorial(y))

def probability(dice_number, sides, target):
    if (target < dice_number) or (target > dice_number*sides):
        return 0.0000
    return round((1/(sides**dice_number))*sum([((-1)**i)*binom(dice_number, i)*binom(target-(i*sides)-1, dice_number-1) for i in range(floor((target-dice_number)/sides)+1)]), 4)
