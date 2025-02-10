#!/usr/bin/python3

"""
Module for Task 1 - write file
"""

def write_file(filename="", text=""):
    """
    Writes into a file and return number of char
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
