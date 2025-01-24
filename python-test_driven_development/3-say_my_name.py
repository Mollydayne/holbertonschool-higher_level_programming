#!/usr/bin/python3

"""This file is the say_my_name function, and not the Destiny's Child song"""


def say_my_name(first_name, last_name=""):

    """Printing first and last name from a given list"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}".strip())
