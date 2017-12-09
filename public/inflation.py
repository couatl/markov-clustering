from public.matrix import normalize, adamar_pow


def inflation(matrix, inflate_factor):
    return normalize(adamar_pow(matrix, inflate_factor))
