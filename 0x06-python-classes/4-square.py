#!/usr/bin/python3
"""square"""


class Square:
    """square"""
    def __init__(self, size=0):
        """square"""
        self.size = size

    @property
    def size(self):
        """square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """squsr"""
        return self.__size * self.__size
