#!/usr/bin/env python3

from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

# Données d'exemple
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Nom du fichier JSON
filename = "data.json"

# Test de la sérialisation
serialize_and_save_to_file(data_to_serialize, filename)
print(f"Data serialized and saved to '{filename}'.")

# Test de la désérialisation
deserialized_data = load_and_deserialize(filename)
print("Deserialized Data:")
print(deserialized_data)
