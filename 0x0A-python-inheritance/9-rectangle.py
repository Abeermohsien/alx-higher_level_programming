#!/usr/bin/python3
"""module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry"""
    def __init__(self, width, height):
        """BaseGeometry"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """str"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
