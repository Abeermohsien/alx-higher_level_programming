#!/usr/bin/python3


class square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("sizr mist be >= 0")
        self.__size = size
