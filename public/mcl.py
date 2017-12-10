# coding=utf8

import time

from public.inflation import inflation
from public.expansion import expansion
from public.matrix import add_self_loops, normalize, \
    converged, rounding

import public.config as config
from public.clusters import get_clusters


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
