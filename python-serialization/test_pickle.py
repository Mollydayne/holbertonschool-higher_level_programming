#!/usr/bin/env python3

from task_01_pickle import CustomObject

obj = CustomObject("John", 25, True)

print("Original Object:")
obj.display()

filename = "custom_object.pkl"
obj.serialize(filename)
print(f"\nObject serialized and saved to '{filename}'.")

loaded_obj = CustomObject.deserialize(filename)
if loaded_obj:
    print("\nDeserialized Object:")
    loaded_obj.display()
else:
    print("\nFailed to deserialize object.")
