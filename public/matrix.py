def normalize(matrix):
    column_sums = []
    for column in zip(*matrix):
        column_sums.append(sum(column))

    normalized = []
    for row in matrix:
        i = 0
        sub_list = []
        for element in row:
            if (column_sums[i] != 0):
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


def pow(matrix, power):
    matrix1 = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    p = power
    turns = 1
    while (1):
        m = p % 2
        p = p / 2

        if m == 1 and turns == 1:
            matrix1 = matrix
            turns = 0
            if p == 0:
                break
            else:
                matrix = multiply(matrix, matrix)
                continue
        if m == 1:
            matrix = multiply(matrix1, matrix)
        if p == 0:
            break

    matrix = multiply(matrix, matrix)

    return matrix
