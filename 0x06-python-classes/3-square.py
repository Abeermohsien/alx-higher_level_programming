#!/usr/bin/python3
"""sqiare"""


class Square:
    """square"""
    def __init__(self, size=0):
        """square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """sqaur"""
        return self.__size * self.__size 
