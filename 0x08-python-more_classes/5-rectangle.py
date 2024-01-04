#!/usr/bin/python3                              """                                             rectangle                                       """                                             
class Rectangle:                                    """rectangle"""                                 def ___init___(self, width=0, height=0):            """rectangle"""                                 self.height = height
        self.width = width                                                                          @property
    def width(self):
        """width"""
        return self.__width
    @width.setter
    def width(self, value):
        """width"""
        if type(value) is not int:
            raise TypeError("width must be an in
teger")                                                 if value < 0:                                       raise ValueError("width must be >= 0
")                                                      self.__width = value                                                                        @property                                       def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):                            """width"""                                     if type(value) is not int:                          raise TypeError("height must be an integer")
        if value < 0:                                       raise ValueError("height must be >= 0")                                                     self.__height = value                                                                           def area(self):                                     """area"""
        def perimeter:
            """perimeter"""                                 if self.__width == 0 or self.__heigh
t == 0:
                return 0                                    return (self.__widtg * 2) + (self.__
height * 2)

        def __str__(self):
            """string"""
            str = ""                                        if self.__width != 0 and self.__height != 0:
                str += "\n".join("#" * self.__width for j in range(self.__height))
                return str
            def __repr__(self):
                """repre"""
                return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
            def __del__(self)
            """del"""
            print("Bye rectangle...")
