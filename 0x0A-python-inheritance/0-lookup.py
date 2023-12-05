#!/usr/bin/python3
"""module to search for methods"""


def lookup(obj):
    """method to return  list of attributes and methods of an object"""
    res = dir(obj)
    return res
