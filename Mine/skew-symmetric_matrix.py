# -*- coding: utf-8 -*-

import numpy as np

def checkio(matrix):
    matrix = np.asarray(matrix)
    return True if (-matrix.T == matrix).all() else False