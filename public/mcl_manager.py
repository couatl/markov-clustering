# coding=utf8

import time

from public.mcl import mcl
from public.clusters import clusters_to_output


def reader(filename):
    matrix = []
    with open(filename) as input_file:
        for r in input_file.readlines():
            values = r.strip().split(",")
            matrix.append([float(x.strip()) for x in values])
    return matrix


def mcl_manager(input_file, output_info='output'):
    matrix = reader(input_file)

    begin_time = time.time()
    matrix, clusters, loops_count = mcl(matrix)
    end_time = time.time()

    print("Вершин в графе: {}".format(len(matrix[0])))
    print("Посчитано за {} секунд".format(end_time - begin_time))
    print("Программа сработала за {} циклов\n".format(loops_count))

    with open(output_info, 'wt') as output_file:
        clusters_to_output(clusters, output_file)
