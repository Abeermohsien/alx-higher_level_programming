#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda mat: list(map(lambda n: n**2, mat)), matrix))
