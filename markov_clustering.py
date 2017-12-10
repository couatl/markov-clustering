# coding=utf8

import sys

from public.solver import solve
from public.matrix import MatrixException

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except:
        raise Exception('Забыли ввести имя файла на вход!')

    output_info = sys.argv[2] if len(sys.argv) > 2 else 'output_info.txt'
    output_graph = sys.argv[3] if len(sys.argv) > 3 else 'output_graph.csv'

    try:
        solve(filename, output_info, output_graph)
    except MatrixException as e:
        print(e.msg)
