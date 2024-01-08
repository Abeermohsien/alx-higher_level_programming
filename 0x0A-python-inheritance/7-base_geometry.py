#!/usr/bin/python3
"""base geometry"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer valider"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            ValueError("{} must be greater than 0".format(name))
