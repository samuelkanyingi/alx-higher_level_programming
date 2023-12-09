#!/usr/bin/python3
"""module to find the class"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor to be called"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
