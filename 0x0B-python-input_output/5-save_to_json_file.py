#!/usr/bin/python3
import json
"""define function that Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    with open(filename, 'w') as a_file:
        json.dump(my_obj, a_file)
