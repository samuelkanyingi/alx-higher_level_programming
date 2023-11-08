#!/usr/bin/python3
"""define function that returns JSON"""
import json


def to_json_string(my_obj):
    """function to return JSON string"""
    return json.dumps(my_obj)
