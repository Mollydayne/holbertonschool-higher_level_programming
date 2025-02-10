#!/usr/bin/python3

"""
Module for task 8 : Class to Json
"""

import json


def class_to_json(obj):
    """
    Returns a dictionnary description
    """

    return obj.__dict__
