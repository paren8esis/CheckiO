# -*- coding: utf-8 -*-

import numpy as np

def check_sequence(row):
    c = row[0]
    count = 1
    for i in row[1:]:
        if (i == c):
            count += 1
            if (count == 4):
                return True
        else:
            count = 1
            c = i
    return False

def checkio(matrix):
    # Check horizontal slices
    matrix = np.asarray(matrix)

    for row in matrix:
        if (check_sequence(row)):
            return True

    # Check vertical slices
    for row in matrix.T:
        if (check_sequence(row)):
            return True

    # Offset for diagonals
    if (len(matrix) - 4 == 0):
        offset_range = range(0,1)
    else:
        offset_range = range(-(len(matrix)-4), len(matrix)-3)

    # Check left-to-right diagonals (\)
    for offset in offset_range:
        if (check_sequence(np.diagonal(matrix, offset))):
            return True

    # Check right-to-left diagonals (/)
    for offset in offset_range:
        if (check_sequence(np.diagonal(matrix[::-1, :], offset))):
            return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert checkio([
#        [1, 2, 1, 1],
#        [1, 1, 4, 1],
#        [1, 3, 1, 6],
#        [1, 7, 2, 5]
#    ]) == True, "Vertical"
#    assert checkio([
#        [7, 1, 4, 1],
#        [1, 2, 5, 2],
#        [3, 4, 1, 3],
#        [1, 1, 8, 1]
#    ]) == False, "Nothing here"
#    assert checkio([
#        [2, 1, 1, 6, 1],
#        [1, 3, 2, 1, 1],
#        [4, 1, 1, 3, 1],
#        [5, 5, 5, 5, 5],
#        [1, 1, 3, 1, 1]
#    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
