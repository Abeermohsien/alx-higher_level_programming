#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_intt True
    try:
        print("{:d}".format(value))
    except Exceptiom as e:
        print("Exception:", e, file=sys.stderr)
        is_intt = False
    return is_intt
