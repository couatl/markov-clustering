# coding=utf8

import time

from public.inflation import inflation
from public.expansion import expansion
from public.matrix import add_self_loops, normalize, \
    converged, rounding

import config
from clusters import get_clusters

def mcl(matrix, expand_factor=config.EXPAND_FACTOR,
        inflate_factor=config.INFLATE_FACTOR,
        max_loop=config.MAX_LOOP,
        loop_value=config.LOOP_VALUE,
        accuracy=config.ACCURACY):
    matrix = add_self_loops(matrix, loop_value)
    matrix = normalize(matrix)

    for i in range(max_loop):
        print("Цикл {}".format(i))
        last_matrix = matrix

        begin_time = time.time()
        matrix = inflation(matrix, inflate_factor)
        print("inflation: {}".format(time.time()-begin_time))

        begin_time = time.time()
        matrix = expansion(matrix, expand_factor)
        print("expansion: {}".format(time.time() - begin_time))

        begin_time = time.time()
        result = converged(matrix, last_matrix)
        print("converged: {}".format(time.time() - begin_time))

        if result:
            print("Программа сработала за {} циклов".format(i))
            break

        begin_time = time.time()
        matrix = rounding(matrix, accuracy)
        print("rounding: {}".format(time.time() - begin_time))


    clusters = get_clusters(matrix)

    return matrix, clusters
