#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """apeend file"""
    with open(filename, "a", encoding="utf-8") as filee:
        return filee.write(text)
