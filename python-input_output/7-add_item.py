#!/usr/bin/python3

"""
Module for task 7 - Load, add, save
"""

import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

"""
Adds all arguments to a list
"""

filename = "add_item.json"
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
