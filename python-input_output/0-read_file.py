#!/usr/bin/python3

"""
Module for Task 0 -  read file
"""


def read_file(filename=""):
    """
    Reads a file and prints its content
    """

    with open("my_file_0.txt", "r") as file:
        content = file.read()
        print(content, end="")
