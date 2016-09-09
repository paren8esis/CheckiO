# -*- coding: utf-8 -*-

def calculate_prob(whites, blacks, step):
    if (step == 1):
        return whites / (whites+blacks)
    if (whites == -1) or (blacks == -1):
        return 0
    return (calculate_prob(whites-1, blacks+1, step-1) * (whites/(whites+blacks))) + (calculate_prob(whites+1, blacks-1, step-1) * (blacks/(whites+blacks)))
        

def checkio(marbles, step):
    whites = marbles.count('w')
    blacks = marbles.count('b')
    
    return float("{0:.2f}".format(calculate_prob(whites, blacks, step)))

if __name__ == '__main__':
    print(checkio('wwwwwbb', 2))