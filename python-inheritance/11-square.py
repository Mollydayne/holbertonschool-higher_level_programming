#!/usr/bin/python3
"""
Module that defines a Square class
inheriting from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    New class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        class attributs for Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        returns the fstring
        """
        return f"[Square] {self.__size}/{self.__size}"
