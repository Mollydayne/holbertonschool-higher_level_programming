#!/usr/bin/python3

"""
Module for Task 5 - Save object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file, using Json
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
