#!/usr/bin/python3
""" define class BaseGeometry"""


class BaseGeometry:
    """base class for geometry operations"""
    def area(self):
        """function to raise error if area is not implemented"""
        raise Exception("area() is not implemented")
