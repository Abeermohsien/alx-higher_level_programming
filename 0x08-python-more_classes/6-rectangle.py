#!/usr/bin/python3
"""
calss rectangle
"""

class Rectangle:
    """4ectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initlize"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """deleyed instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
            """height """
            return self.__height
