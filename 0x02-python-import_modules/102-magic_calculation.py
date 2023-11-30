#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        n = add(a, b)
        for j in range(4, 6):
            n = add(n, j)
        return n
    else:
        return sub(a, b)
    return 0
