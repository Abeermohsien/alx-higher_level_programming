#!/usr/bin/python3
"""python"""


def pascal_triangle(n):
    """pascal"""
    if n <= 0:
        return []

    triang = [[1]]
    while len(triang) != n:
        trin = triang[-1]
        tmp = [1]
        for j in range(len(trin) - 1):
            tmp.append(trin[j] + trin[j] + 1])
        tmp.append(1)
        triang.append(tmp)
    return triang
