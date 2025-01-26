#!/usr/bin/python3
def roman_to_int(roman_string):

    romanDictionnary = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    buffer = 0
    for char in roman_string:
        value = romanDictionnary.get(char, 0)
    if value > buffer:
        total += value
    buffer = value
    return total
