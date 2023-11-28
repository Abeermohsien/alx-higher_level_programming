#!/usr/bin/python3
def remove_char_at(str, n):
    nstr = ""
    for j, ch in enumerate(str):
        if j != n:
            nstr += ch
    return nstr
