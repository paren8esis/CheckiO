import math

def checkio(data):
    data.sort()
    res = 0
    foo = len(data) / 2
    mid = math.floor(foo)
    if (mid == foo):
    # Even number of elements
        res = (data[mid-1] + data[mid]) / 2
    else:
    # Odd number of elements
        res = data[mid]
    
    return res
