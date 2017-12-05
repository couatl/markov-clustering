#!/usr/bin/env python

import sys
from public.matrix import normalize, multiply, pow
from public.reader import reader

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except:
        raise Exception('Enter input filename!')
    m = reader(filename)
    print m
    print normalize(m)
    print multiply(m, m)
    print pow(m, 3)