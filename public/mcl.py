from public.inflation import inflation
from public.expansion import expansion
from public.matrix import add_self_loops, normalize, \
    converged, rounding

import config


def mcl(matrix, expand_factor=config.EXPAND_FACTOR,
        inflate_factor=config.INFLATE_FACTOR,
        max_loop=config.MAX_LOOP,
        loop_value=config.LOOP_VALUE,
        accuracy=config.ACCURACY):
    matrix = add_self_loops(matrix, loop_value)
    matrix = normalize(matrix)

    for i in range(max_loop):
        lastMatrix = matrix
        matrix = inflation(matrix, inflate_factor)
        matrix = expansion(matrix, expand_factor)
        if converged(matrix, lastMatrix):
            # Написать номер цикла завершения
            break
        matrix = rounding(matrix, accuracy)

    return matrix
