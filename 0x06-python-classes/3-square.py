#!/usr/bin/python3
"""sqiare"""


class square:
    """square"""
    def __int__(self, size=0):
        """square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """sqaur"""
        return self.__size ** 2
