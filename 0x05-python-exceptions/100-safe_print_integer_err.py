#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_in = True
    try:
        print("{:d}".format(value))
    except Exceptiom as error:
        print("Exception:", error, file=sys.stderr)
        is_in = False
    return is_in
