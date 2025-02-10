#!/usr/bin/python3

"""
Module for Task 0 -  read file
"""


def read_file(filename=""):
    """
    Reads a file and prints its content
    """

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
