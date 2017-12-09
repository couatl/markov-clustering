def reader(filename):
    matrix = []
    for r in open(filename):
        r = r.strip().split(",")
        matrix.append(list(map(lambda x: float(x.strip()), r)))

    return matrix
