#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    int1 = tuple_a[0] if len(tuple_a) > 0 else 0
    int2 = tuple_a[1] if len(tuple_a) > 1 else 0
    int3 = tuple_b[0] if len(tuple_b) > 0 else 0
    int4 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (int1 + int3, int2 + int4)
