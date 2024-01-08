#!/usr/bin/python3
"""module"""


class MyInt(int):
    """module"""
    def __new__(clss, *ars, **kars):
        """module"""
        return super(MyInt, clss).__new__(clss, *ars, **kars)

    def __eq__(self, other):
        """module"""
        return int(self) != other

    def __ne__(self, other):
        """module"""
        return int(self) == other
