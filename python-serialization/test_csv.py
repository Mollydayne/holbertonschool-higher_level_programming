#!/usr/bin/env python3

from task_02_csv import convert_csv_to_json

# Nom du fichier CSV à convertir
csv_file = "data.csv"

# Lancement de la conversion
if convert_csv_to_json(csv_file):
    print(f"Les données de {csv_file} ont été converties en data.json")
else:
    print("Échec de la conversion.")
