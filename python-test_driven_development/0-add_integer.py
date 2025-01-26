#!/usr/bin/python3

"""This file is the add_integer fonction"""


def add_integer(a, b=98):

    """Purpose of this function : adding two intergers; one of them is 98"""

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    b = int(b)
    a = int(a)
    return a + b
