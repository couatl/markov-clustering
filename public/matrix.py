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
    matrix = [[0 for i in range(len(a))] for j in range(len(b))]
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                matrix[i][j] += a[i][k] * b[k][j]

    return matrix


def adamar_pow(matrix, power):
    buffer = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            buffer[i][j] += matrix[i][j] ** power

    return buffer


def matrix_pow(matrix, power):
    result = matrix
    for i in range(1, power):
        result = multiply(result, matrix)
    return result


def add_self_loops(matrix, loop_value):
    rows = len(matrix)
    columns = len(matrix[0])

    if rows != columns:
        raise MatrixException(ErrorMessages.NOT_SQUARED)

    for i in range(len(matrix)):
        matrix[i][i] = loop_value

    return matrix


def converged(a, b, accuracy=1e-04):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] - b[i][j] >= accuracy:
                return False
    return True

# def matrix_pow(matrix, power):
#     buffer = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
#     turns = 1
#     while (1):
#         m = power % 2
#         power = power / 2
#
#         if m == 1 and turns == 1:
#             buffer = matrix
#             turns = 0
#             if power == 0:
#                 break
#             else:
#                 matrix = multiply(matrix, matrix)
#                 continue
#         if m == 1:
#             matrix = multiply(buffer, matrix)
#         if power == 0:
#             break
#
#     matrix = multiply(matrix, matrix)
#
#     return matrix
