import json

def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    data = {"name": "John Doe","age": 30,"city": "New York"}

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open("data.json", "r") as file:
        loaded_data = json.load(file)

    print(loaded_data)
