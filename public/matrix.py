# coding=utf8


class MatrixException(Exception):
    def __init__(self, msg):
        self.msg = msg


class ErrorMessages:
    NOT_SQUARED = 'Матрица графа неквадратная! Проверьте, все ли верно.'


def normalize(matrix):
    column_sums = []
    for column in zip(*matrix):
        column_sums.append(sum(column))

    normalized = []
    for row in matrix:
        i = 0
        sub_list = []
        for element in row:
            if column_sums[i] != 0:
                sub_list.append(float(element) / column_sums[i])
            else:
                sub_list.append(float(element))
            i += 1
        normalized.append(sub_list)

    return normalized


def multiply(a, b):
    length = len(a)
    matrix = [[0 for i in range(length)] for j in range(length)]

    for i in range(len(a)):
        for k in range(len(a)):
            if a[i][k]:
                for j in range(len(a)):
                    matrix[i][j] += a[i][k] * b[k][j]
    return matrix


def adamar_pow(matrix, power):
    buffer = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            buffer[i][j] += matrix[i][j] ** power

    return buffer


def add_self_loops(matrix, loop_value):
    rows = len(matrix)
    columns = len(matrix[0])

    if rows != columns:
        raise MatrixException(ErrorMessages.NOT_SQUARED)

    for i in range(len(matrix)):
        matrix[i][i] = loop_value

    return matrix


def rounding(matrix, accuracy):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] <= accuracy:
                matrix[i][j] = 0
    return matrix


def converged(a, b):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] - b[i][j] != 0:
                return False
    return True