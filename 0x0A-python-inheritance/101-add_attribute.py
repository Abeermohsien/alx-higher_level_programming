#!/usr/bin/python3
"""moduel"""


def add_attribute(ob, at, val):
    """module"""
    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, at, val)
