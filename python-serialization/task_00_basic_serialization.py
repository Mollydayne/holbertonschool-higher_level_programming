#!/usr/bin/python3

"""
Module for task 0 - Basic Serialization
"""

import json

def serialize_and_save_to_file(data, filename):
    data = {"name": "John Doe","age": 30,"city": "New York"}

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    with open("data.json", "r") as file:
        loaded_data = json.load(file)

    print(loaded_data)
