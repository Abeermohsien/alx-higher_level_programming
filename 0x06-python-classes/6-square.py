#!/usr/bin/python3
"""squre"""


class Square:
    """squre"""
    def __init__(self, size=0, position(0, 0)):
        """squre"""
        self.size = size
        self.position = position

    @property 
    def size(self):
        """squre"""
        return (self.__size)

    @size.setter 
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """squre"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                not all(num >= 0 for num in value) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """squre"""
        return (self.__size ** 2)

    def my_print(self):
        """sqire"""
        if self.__size == 0:
            print("")
            return

        [print("") for n in range(0, self.__position[1])]
        for n in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
