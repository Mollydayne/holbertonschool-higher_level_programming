#!/usr/bin/python3

"""
Module for Task 2 - append to a file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
