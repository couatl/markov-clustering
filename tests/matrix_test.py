#!/usr/bin/env python

# python -m unittest tests.matrix_test

import unittest

from public.matrix import normalize, adamar_pow, multiply,\
    matrix_pow, add_self_loops, converged

class MatrixTest(unittest.TestCase):
    def test_normalize(self):
        test_matrix = [[1, 1, 0],
                       [0, 1, 1],
                       [0, 0, 1]]

        result_matrix = [[1, 0.5, 0],
                         [0, 0.5, 0.5],
                         [0, 0, 0.5]]

        self.assertEqual(normalize(test_matrix), result_matrix)

    def test_adamar_pow(self):
        test_matrix = [[2, 1, 0],
                       [1, 2, 3],
                       [0, 0, 0.5]]

        result_matrix = [[4, 1, 0],
                         [1, 4, 9],
                         [0, 0, 0.25]]

        self.assertEqual(adamar_pow(test_matrix, 2), result_matrix)

    def test_multiply(self):
        test_matrixA = [[2, 1, 0],
                        [1, 2, 3],
                        [0, 0, 1]]

        test_matrixB = [[1, 1, 0],
                        [1, 0, 3],
                        [0, 0, 1]]

        result_matrix = [[3, 2, 3],
                         [3, 1, 9],
                         [0, 0, 1]]

        self.assertEqual(multiply(test_matrixA, test_matrixB), result_matrix)

    def test_matrix_pow(self):
        test_matrix = [[2, 1, 0],
                       [1, 2, 3],
                       [1, 1, 1]]

        result_matrix = [[17, 16, 15],
                         [31, 32, 33],
                         [16, 16, 16]]

        self.assertEqual(matrix_pow(test_matrix, 3), result_matrix)

    def test_add_self_loops(self):
        test_matrix = [[0, 1, 0],
                       [1, 0, 3],
                       [1, 1, 1]]

        result_matrix = [[2, 1, 0],
                         [1, 2, 3],
                         [1, 1, 2]]

        self.assertEqual(add_self_loops(test_matrix, 2), result_matrix)

    def test_converged(self):
        test_matrix = [[0.03, 1, 0],
                       [1, 0, 3],
                       [0.0008, 1, 1]]

        self.assertEqual(converged(test_matrix, test_matrix), True)

    def test_converged_accuracy(self):
        test_matrixA = [[0.03, 1, 0],
                       [1, 0, 3],
                       [0.0008, 1, 1]]

        test_matrixB = [[0.03005, 1, 0],
                       [1, 0, 3],
                       [0.00087, 1, 1]]

        self.assertEqual(converged(test_matrixA, test_matrixB, 1e-3), True)

if __name__ == '__main__':
    unittest.main()
