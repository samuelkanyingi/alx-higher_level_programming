#!/usr/bin/python3
"""convert Objet to a dictionary"""


def class_to_json(obj):
    """function that returns the dictionary description"""
    if isinstance(obj, MyClass):
        data = {
                "__class__": "MyClass",
                "name": obj.name,  "number": obj.number}
        return data
