#!/usr/bin/python3
def uppercase(str):
    for char in str:
        asciiVal = ord(char)
        upperChar = chr(asciiVal - 32) if 97 <= asciiVal <= 122 else char
        print("{}".format(upperChar), end="")
    print()
