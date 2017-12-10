# coding=utf8

import time
import csv

from public.mcl import mcl
from public.clusters import clusters_to_output
from public.reader import reader


def solver(input_file, output_info='output_info.txt', output_graph='output_graph.csv'):
    matrix = reader(input_file)

    begin_time = time.time()
    matrix, clusters, loops_count = mcl(matrix)
    end_time = time.time()

    with open(output_graph, 'wt') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(matrix)

    with open(output_info, 'wt') as output_file:
        output_file.write("Вершин в графе: {}\n".format(len(matrix[0])))
        output_file.write("Посчитано за {} секунд\n".format(end_time - begin_time))
        output_file.write("Программа сработала за {} циклов\n".format(loops_count))
        clusters_to_output(clusters, output_file)