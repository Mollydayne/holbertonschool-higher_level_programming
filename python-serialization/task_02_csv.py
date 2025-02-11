#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file
    """

    try:
        with open(csv_filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Conversion réussie !")
        return True

    except FileNotFoundError:
        print(f"Erreur : le fichier '{csv_filename}' n'existe pas.")
        return False
