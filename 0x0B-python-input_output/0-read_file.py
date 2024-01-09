#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read fike"""
    with open(filename, encoding="utf-8") as filee:
        print(filee.read(), end="")
