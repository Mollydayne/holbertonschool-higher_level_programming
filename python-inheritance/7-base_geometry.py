#!/usr/bin/python3

"""Following of basegeometry class"""


class BaseGeometry:

    """
    Basegeometry class
    """
    def area(self):
        """
        raising an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
