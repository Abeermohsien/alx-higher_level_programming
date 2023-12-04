#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for subm in matrix:
        if len(subm) == 0:
            print()
        for j in range(len(subm)):
            if j is len(subm) - 1:
                print("{:d}".format(subm[j]), end="\n")
            else:
                print("{:d}".format(subm[j]), end=" ")
