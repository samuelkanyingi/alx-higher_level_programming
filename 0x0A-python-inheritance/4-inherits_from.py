#!/usr/bin/python3
""" defines a function is a subclass"""


def inherits_from(obj, a_class):
    """check if object is instance of class inherited
    Args:
        obj:object
        a_class: class to compare with
    Return: True if an object is a subclass
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
