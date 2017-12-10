# coding=utf8

import sys

from public.mcl_manager import mcl_manager
from public.matrix import MatrixException

if __name__ == '__main__':


    try:
        filename = sys.argv[1]
    except:
        raise Exception('Забыли ввести имя файла на вход!')

    output = sys.argv[2] if len(sys.argv) > 2 else 'output'

    try:
        mcl_manager(filename, output)
    except MatrixException as e:
        print(e.msg)
