#!/usr/bin/python3
'''rectangle class'''
                                                class Rectangle:
    """rectangle"""
                                                    number_of_instances = 0                         """num of instance"""
                                                    print_symbol = '#'                              """print symbol"""                                                                              def __init__(self, width=0, height=0):              """ininlize"""                                  self.width = width
        self.height = hight                             Rectangle.number_of_instances += 1      
    @property
    def width(self):                                    """width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):                      raise TypeError("width must be an in
teger")
        if value < 0:
            raise ValueError("width must be >= 0
")
                                                    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isintance(value, int):
            raise TypeError("height must be an i
nteger")
        if value < 0:
            raise ValueError("height must be >=
0")
        self.__height = value

        def area(self):
            """area"""                                      return self.width * self.height

        def perimeter(self):                                """perimeter"""
            if not self.width or not self.height
:
                return 0
            return (self.width + self.height) * 2
                                                        def __str__(self):                                  """string"""                                    if not self.width or not self height
:                                                               return ""                                   return ((str(self.print_symbol) * self.width + "\n") *                                                  self.height)[:-1]
def __repr__(self):
                """repr"""
                return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

            def __del__(self):
                """delet"""
                print("Bye rectangle...")
                Rectangle.number_of_instances -= 1
            @staticmethod
            def bigger_or_equal(rect_1, rect_2):
                """bigger"""
                if not isintance(rect_1, Rectangle):
                    raise TypeError("rect_1 must be an instance of Rectangle")
                if not isintance(rect_2, Rectangle):
                    raise TypeError("rect_2 must be an instance of Rectangle")
                if rect_2.area() > rect_1.area():
                    return rect_2
                return rect_1
