#!/usr/bin/python3

"""
Module for task 3
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python
    """
    try:
        # Charger le fichier XML
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {child.tag: child.text for child in root}

        return dictionary
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ET.ParseError:
        print(f"Error: Failed to parse '{filename}'.")
        return None
