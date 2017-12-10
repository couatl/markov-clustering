# coding=utf8

import sys

from public.solver import solve
from public.matrix import MatrixException

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except:
        raise Exception('Забыли ввести имя файла на вход!')

    output = sys.argv[2] if len(sys.argv) > 2 else 'output'

    try:
        solve(filename, output)
    except MatrixException as e:
        print(e.msg)
