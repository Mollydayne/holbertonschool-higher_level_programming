#!/usr/bin/python3
def no_c(my_string):
    unwantedChar = ['c', 'C']
    new_string = ""
    for char in my_string:
        if char not in unwantedChar:
            new_string += char
    return new_string
