#!/usr/bin/python3

"""
Module for task 0 - Basic Serialization
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary and saves it to a JSON file
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file
    """
    with open(filename, "r") as file:
        return json.load(file)
