#!/usr/bin/python3

"""This file is the text_indentation function"""


def text_indentation(text):

    """The purpose is to print a text with two new lines after each of defined chars : . , ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result =""
    for char in text:
        result += char
        if char in ".?:":
            print(result.strip())
            print()
            result =""
    if result:
        print (result.strip())
