#!/usr/bin/python3
"""define class BaseGeometry"""


class BaseGeometry:
    """calculate area"""
    def area(self):
        """function that raise error if area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate an integer value
        Args:
            name:string
            value: integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
