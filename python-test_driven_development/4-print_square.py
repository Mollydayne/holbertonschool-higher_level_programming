#!/usr/bin/python3

"""This file is the print_square function"""


def print_square(size):

    """The idea is to print a square using # """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
    print()
