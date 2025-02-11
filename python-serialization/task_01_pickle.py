#!/usr/bin/python3

"""
Module for task 1 : Pickling Custom Classes
"""

import pickle


class CustomObject:
    """
    Class that defines a CustomObject
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Method to print object attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file and returns an instance of CustomObject.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (OSError, IOError, pickle.UnpicklingError) as e:
            print(f"Error deserializing object: {e}")
            return None
