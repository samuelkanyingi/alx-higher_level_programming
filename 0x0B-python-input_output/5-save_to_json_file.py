#!/usr/bin/python3
"""module to find method"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
