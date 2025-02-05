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
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
