#!/usr/bin/python3
"""find class geometry in module"""


class BaseGeometry:
    """base class"""

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate  a value given"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """inherits from baseclass"""

    def __init__(self, width, height):
        """class constructor to initialize width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    def area(self):
        """calculate area"""
        return self.__width * self.__height
    
    def __str__(self):
        """string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def print(self):
        """print rectangle"""
        print(str(self))
