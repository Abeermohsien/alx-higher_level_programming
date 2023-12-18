#!/usr/bin/python3
def magic_calculation(a, b):
    n = 0
    for j in range(1, 3):
        try:
            if j < a:
                raise Exception("Too far")
            n += a ** b / j
        except Exception:
            n = b + a
            break
    return n
