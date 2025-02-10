#!/usr/bin/python3

"""
Module for task 10 : Student to Json with filter
"""


class Student:
    """
    Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            filtered_dict = {}
            for attr in attrs:
                if type(attr) is str and hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict
        return self.__dict__
