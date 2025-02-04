#!/usr/bin/python3

"""Class checker"""


def is_same_class(obj, a_class):

    """return true if it's an instance of the class"""

    if isinstance(obj, a_class):
        return type(obj) is a_class
