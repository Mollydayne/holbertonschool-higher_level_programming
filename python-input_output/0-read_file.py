#!/usr/bin/python3

"""
Task 0
"""


def read_file(filename=""):
    """
    Reads a file and prints its content
    """

    with open("my_file_0.txt", "r") as file:
        content = file.read()
        print(content, end="")
