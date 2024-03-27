#!/usr/bin/python3
"""
Find the peaking
"""


def find_peak(list_of_integers):
    """
    Return a list of ints of peaks
    """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
