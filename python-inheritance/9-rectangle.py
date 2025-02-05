#!/usr/bin/python3
"""
Module that defines a Rectangle class
inheriting from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    New class that inherits from the first one
    """

    def __init__(self, width, height):
        """
        class attributs for rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns the area of a retangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns a fstring of rectangle
        """
        return f"[rectangle] {self.__width}/{self.__height}"
