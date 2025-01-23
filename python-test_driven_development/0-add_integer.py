#!/usr/bin/python3

"""This file is the add_integer fonction"""

def add_integer(a, b=98):

    """Purpose of this function : adding two intergers; one of them is 98"""

    try:
        return a+b
        sum = add(a, b)

    except TypeError:
        print("a must be an integer")
    finally:
        return a+b
        sum = add(a, b)
        print(sum)
