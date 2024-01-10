#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    res = []
    for arr in matrix:
        res.append(list(map(lambda x: x*x, arr)))
    return res
