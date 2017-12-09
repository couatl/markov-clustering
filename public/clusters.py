# coding=utf8

def get_clusters(matrix):
    clusters = []

    for i in range(len(matrix)):
        if matrix[i][i] and matrix[i] not in clusters:
            clusters.append(matrix[i])

    clust_map = {}
    for cn, c in enumerate(clusters):
        for x in [i for i, x in enumerate(c) if x]:
            clust_map[cn] = clust_map.get(cn, []) + [x]
    return clust_map


def clusters_to_output(clusters):
    print("Кластеры:")
    for k, v in clusters.items():
        print('{}, {}'.format(k, v))
