#!/usr/bin/python3

"""
Class for the circle task
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    """
    area and perimeter
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    """
    circle calculations
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius * self.radius)

    def perimeter(self):
        return abs((2 * self.radius) * pi)


class Rectangle(Shape):
    """
    Rectangle!
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
