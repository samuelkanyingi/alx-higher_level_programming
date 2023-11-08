#!/usr/bin/python3
"""define function that convert From JSON string to Object"""
import json


def from_json_string(my_str):
    """function to return an object represented by a JSON string"""
    return json.loads(my_str)
