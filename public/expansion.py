from matrix import matrix_pow

import numpy as np

def expansion(matrix, expand_factor):
    return np.linalg.matrix_power(matrix, expand_factor)
    # return matrix_pow(matrix, expand_factor)
