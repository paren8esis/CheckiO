# -*- coding: utf-8 -*-

def bitwise_rotR(num, n, max_n):
    n = n % max_n
    return (num >> n) | ((num & ((2**n) - 1)) << (max_n - n))

def rotate(state, pipe_numbers):
    max_n = len(state)
    target = [0] * len(state)
    # Convert list to binary string
    state = int(''.join([str(x) for x in state]), 2)
    # Define the target binary string
    for cannon in pipe_numbers:
        target[cannon] = 1
    target = int(''.join([str(x) for x in target]) ,2)

    # Find all possible rotations
    rotations = []
    for i in range(0, max_n):
        if (bitwise_rotR(state, i, max_n) & target == target):
            rotations.append(i)

    return rotations