# -*- coding: utf-8 -*-

from math import trunc
from decimal import Decimal

def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):   
    power = 0
    number = Decimal(number)
    while (abs(number) >= base) and (power < len(powers)-1):
        number = number / base
        power += 1

    if (decimals == 0):
        res = str(trunc(number))
    else:
        if ('.' not in str(number)):
            res = str(number) + '.' + ('0' * decimals)
        else:
            res = str(round(number, decimals))
            res += '0' * (decimals - len(res.split('.')[1]))
    res += powers[power] + suffix
        
    return res