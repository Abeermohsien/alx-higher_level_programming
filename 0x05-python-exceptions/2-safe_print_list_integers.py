#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    m = 0
    while m is not x:
        try:
            print("{:d}".format(my_list[m]), end='')
            n += 1
        except (ValueError, TypeError):
            pass
        m += 1
    print()
    return n
