#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes into a file and return number of char
    """

    with open("my_first_file.txt", "w") as file:
        file.writelines("")
