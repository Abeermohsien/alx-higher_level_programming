#!/usr/bin/python3
"""module"""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """module"""
    def __init__(self, size):
        """modulw"""
        self.integer_validator("size", size)
        self.__size = size
        super().__int__(size, size)

    def area(self):
        """module"""
        return self.__size ** 2
