#!/usr/bin/python3
'''rectangle class'''


class Rectangle:
    """rectangle"""

    number_of_instances = 0
    """num of instance"""

    print_symbol = '#'
    """print symbol"""

    def __init__(self, width=0, height=0):
        """ininlize"""
        self.width = width
        self.height = hight
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isintance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        def area(self):
            """area"""
            return self.width * self.height

        def perimeter(self):
            """perimeter"""
            if not self.width or not self.height:
                return 0
            return (self.width + self.height) * 2

        def __str__(self):
            """string"""
            if not self.width or not self height:
                return ""
            return ((str(self.print_symbol) * self.width + "\n") *
                    self.height)[:-1]

        def __repr__(self):
            """repr"""
            str1 = str(self.width)
            str2 = str(self.height)
            return "Rectangle(" + str1 + ", " + str2 + ")"

        def __del__(self):
            """delet"""
            print("Bye rectangle...")
            Rectangle.number_of_instances -= 1
