# coding=utf8

import time

from public.matrix import add_self_loops, normalize, \
    converged, rounding, adamar_pow, multiply
from public.clusters import get_clusters
import public.config as config


def expansion(matrix):
    return multiply(matrix, matrix)


def inflation(matrix, inflate_factor):
    return normalize(adamar_pow(matrix, inflate_factor))


def mcl(matrix, inflate_factor=config.INFLATE_FACTOR,
        max_loop=config.MAX_LOOP,
        loop_value=config.LOOP_VALUE,
        accuracy=config.ACCURACY):
    matrix = add_self_loops(matrix, loop_value)
    matrix = normalize(matrix)

    for i in range(max_loop):
        last_matrix = matrix

        matrix = inflation(matrix, inflate_factor)
        matrix = expansion(matrix)

        if converged(matrix, last_matrix):
            break
        matrix = rounding(matrix, accuracy)

    clusters = get_clusters(matrix)

    return matrix, clusters, i
