# coding=utf8

import sys
import time
import csv

from public.mcl import mcl
from public.clusters import clusters_to_output
from public.reader import reader

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except:
        raise Exception('Забыли ввести имя файла на вход!')

    matrix = reader(filename)

    begin_time = time.time()
    matrix, clusters, loops_count = mcl(matrix)
    end_time = time.time()

    output_info = sys.argv[2] if len(sys.argv) > 2 else 'output_info.txt'
    output_graph = sys.argv[3] if len(sys.argv) > 3 else 'output_graph.csv'

    with open(output_info, 'wt') as output_file:
        output_file.write("Вершин в графе: {}\n".format(len(matrix[0])))
        output_file.write("Посчитано за {} секунд\n".format(end_time - begin_time))
        output_file.write("Программа сработала за {} циклов\n".format(loops_count))
        clusters_to_output(clusters, output_file)

    with open(output_graph, 'wt') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(matrix)
