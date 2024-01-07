#!/usr/bin/python3
"""method"""


def matrix_divided(matrix, div):
    """divides all elemenys"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " + "of integers/floats")
    for ro in matrix:
        if not isinstance(ro, list) or len(ro) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " + "of integers/floats")
        if len(ro) != len(matrix[0]):
            raise TypeErro("Each row of the matrix must have the same size")
        for y in ro:
            if not isinstance(y, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " + "of integers/floats")
    return [[round(y / div, 2) for y in ro] for ro in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
