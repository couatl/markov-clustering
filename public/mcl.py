# coding=utf8


from public.matrix import add_self_loops, normalize, \
    converged, rounding, normalize, adamar_pow, matrix_pow
from public.clusters import get_clusters
import public.config as config


def expansion(matrix, expand_factor):
    return matrix_pow(matrix, expand_factor)


def inflation(matrix, inflate_factor):
    return normalize(adamar_pow(matrix, inflate_factor))


def mcl(matrix, expand_factor=config.EXPAND_FACTOR,
        inflate_factor=config.INFLATE_FACTOR,
        max_loop=config.MAX_LOOP,
        loop_value=config.LOOP_VALUE,
        accuracy=config.ACCURACY):
    matrix = add_self_loops(matrix, loop_value)
    matrix = normalize(matrix)

    for i in range(max_loop):
        last_matrix = matrix
        matrix = inflation(matrix, inflate_factor)
        matrix = expansion(matrix, expand_factor)

        if converged(matrix, last_matrix):
            break
        matrix = rounding(matrix, accuracy)

    clusters = get_clusters(matrix)

    return matrix, clusters, i
