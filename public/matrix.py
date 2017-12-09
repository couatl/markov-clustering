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
        result = strassen_multiplication(result, matrix)
    return result


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


def add(a, b):
    length = len(a)
    c = [[0 for x in range(length)] for y in range(length)]

    for i in range(0, length):
        for j in range(0, length):
            c[i][j] = a[i][j] + b[i][j]

    return c


def subtract(a, b):
    length = len(a)
    c = [[0 for x in range(length)] for y in range(length)]

    for i in range(0, length):
        for j in range(0, length):
            c[i][j] = a[i][j] - b[i][j]

    return c


def strassen_multiplication(a, b):
    length = len(a)
    c = [[0 for x in range(length)] for y in range(length)]

    leaf = 128
    if length < leaf:
        return multiply(a, b)
    else:
        a11 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        a12 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        a21 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        a22 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        b11 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        b12 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        b21 = [[0 for x in range(length / 2)] for y in range(length / 2)]
        b22 = [[0 for x in range(length / 2)] for y in range(length / 2)]

        for i in range(0, length / 2):
            for j in range(0, length / 2):
                a11[i][j] = a[i][j]
                a12[i][j] = a[i][j + (length / 2)]
                a21[i][j] = a[i + (length / 2)][j]
                a22[i][j] = a[i + (length / 2)][j + (length / 2)]
                b11[i][j] = b[i][j]
                b12[i][j] = b[i][j + (length / 2)]
                b21[i][j] = b[i + (length / 2)][j]
                b22[i][j] = b[i + (length / 2)][j + (length / 2)]

        p1 = strassen_multiplication(a11, subtract(b12, b22))
        p2 = strassen_multiplication(add(a11, a12), b22)
        p3 = strassen_multiplication(add(a21, a22), b11)
        p4 = strassen_multiplication(a11, subtract(b21, b11))
        p5 = strassen_multiplication(add(a11, a22), add(b11, b12))
        p6 = strassen_multiplication(subtract(a12, a22), add(b21, b22))
        p7 = strassen_multiplication(subtract(a11, a21), add(b11, b12))

        c11 = add(subtract(add(p5, p4), p2), p6)  # c11 = p5 + p4 - p2 + p6
        c12 = add(p1, p2)  # c12 = p1 + p2
        c21 = add(p3, p4)  # c21 = p3 + p4
        c22 = subtract(subtract(add(p5, p1), p3), p7)  # c22 = p5 + p1 - p3 - p7

        for i in range(0, length / 2):
            for j in range(0, length / 2):
                c[i][j] = c11[i][j]
                c[i][j + (length / 2)] = c12[i][j]
                c[i + (length / 2)][j] = c21[i][j]
                c[i + (length / 2)][j + (length / 2)] = c22[i][j]

        return c

# def matrix_pow(matrix, p):
#     buffer = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
#     turns = True
#     power = p
#     while True:
#         m = power % 2
#         power = int(power / 2)
#
#         if m == 1 and turns and power != 0:
#             buffer = matrix
#             turns = False
#             matrix = multiply(matrix, matrix)
#             continue
#         if m == 1:
#             matrix = multiply(buffer, matrix)
#         if power == 0:
#             break
#         matrix = multiply(matrix, matrix)
#
#     return matrix
