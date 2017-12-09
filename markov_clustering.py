# coding=utf8

import sys
import time

from public.mcl import mcl
from public.clusters import clusters_to_output
from public.reader import reader

import numpy as np

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except:
        raise Exception('Забыли ввести имя файла на вход!')
    matrix = reader(filename)

    print("Вершин в графе: {}".format(len(matrix[0])))

    begin_time = time.time()
    matrix, clusters = mcl(matrix)
    end_time = time.time()

    print("Посчитано за {} секунд".format(end_time-begin_time))
    print("Получившийся граф: ")
    print(np.array(matrix))

    clusters_to_output(clusters)