from math import acos, degrees

def checkio(a, b, c):
    if (a == 0 or b ==0 or c ==0):
        return [0, 0, 0]
    # Use the cosine rule to find angles A, B and C
    try:
        A = round(degrees(acos(((b**2) + (c**2) - (a**2))/(2 * b * c))))
        B = round(degrees(acos(((a**2) + (c**2) - (b**2))/(2 * a * c))))
        C = round(degrees(acos(((a**2) + (b**2) - (c**2))/(2 * a * b))))
    except ValueError:
        return [0, 0, 0]

    # Check that all angles are greater than zero
    if (A == 0 or B == 0 or C == 0):
        return [0, 0, 0]
    # Check that A + B + C = 180 holds
    if (A + B + C == 180):
        return sorted([A, B, C])
    else:
        return [0, 0, 0]

