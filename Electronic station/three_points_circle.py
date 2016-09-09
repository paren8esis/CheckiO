# -*- coding: utf-8 -*-

from math import sqrt

def checkio(data):
    [a1, a2, b1, b2, c1, c2] = data.replace('(', '').replace(')', '').split(',')
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)
    c1 = int(c1)
    c2 = int(c2)

    d = ((a1 - b1) * (b2 - c2)) - ((b1 - c1) * (a2 - b2))
    u = ((a1**2) - (b1**2) + (a2**2) - (b2**2)) / 2
    v = ((b1**2) - (c1**2) + (b2**2) - (c2**2)) / 2

    # Centre coordinates
    x = ((u * (b2 - c2)) - (v * (a2 - b2))) / d
    y = ((v * (a1 - b1)) - (u * (b1 - c1))) / d

    # Radius
    r = round(sqrt(((x - a1)**2) + ((y - a2)**2)), 2)
    return "(x-" + str(round(x,2)).rstrip('0').rstrip('.') + ")^2+(y-" + str(round(y,2)).rstrip('0').rstrip('.') + ")^2=" + str(r).rstrip('0').rstrip('.') + "^2"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

    assert checkio("(6,6),(2,9),(1,6)") == "(x-3.5)^2+(y-6.83)^2=2.64^2"