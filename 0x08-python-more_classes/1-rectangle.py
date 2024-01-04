#!/usr/bin/python3
"""
define clads rectangle
"""


class Rectangle:
    """rectangle"""
    def __init__(self, width=0, height=0):
        """rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
