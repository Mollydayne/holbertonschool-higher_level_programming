#!/usr/bin/python3

"""This is the class of a square"""


class Square:

    """This will later print a square"""

    def __init__(self, size=0):
        """Private attribute for size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
