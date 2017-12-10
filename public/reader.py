def reader(filename):
    matrix = []
    with open(filename) as input_file:
        for r in input_file.readlines():
            values = r.strip().split(",")
            matrix.append([float(x.strip()) for x in values])
    return matrix
