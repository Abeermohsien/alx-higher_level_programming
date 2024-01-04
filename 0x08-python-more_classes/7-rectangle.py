#!/usr/bin/python3
""""
calculate area
"""


class Rectangle:
    """rectangle"""

    number_of_instance = 0
    """self"""

    print_symbol = '#'
    """sumbil"""

    def __init__(self, width=0, height=0):
        """rectanglr"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        """hwoght"""
        return self.__height

    @height.setter
    def height(self, value):
        """height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """self"""
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """self"""
        return "Rectangle({}, {})".format(str(self.width), str(self.height))

    def __del__(self):
        """self"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
