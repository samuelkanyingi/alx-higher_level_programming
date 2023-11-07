#!/usr/bin/python3
"""module to check class instance"""


def is_same_class(obj, a_class):
    """function to true if its instance of class
    Args:
        obj:object
        a_class:class to match with
    Returns: true if object is exactly an instance of the specified class
    """
    return type(obj) is a_class
