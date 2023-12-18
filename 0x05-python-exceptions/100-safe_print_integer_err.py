#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    i_intt = True
    try:
        print("{:d}".format(value))
    except Exceptiom as e:
        print("Exception:", e, file=sys.stderr)
        i_intt = False
    return is_intt
