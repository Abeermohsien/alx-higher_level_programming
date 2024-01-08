#!/usr/bin/python3
"""module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """module"""
    def __init__(self, size):
        """module"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """modula"""
        return self.__size ** 2

    def __str__(self):
        """module"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
