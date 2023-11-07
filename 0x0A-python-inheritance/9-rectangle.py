#!/usr/bin/python3
"""define class geometry"""


class BaseGeometry:
    """define class geometry operations"""
    def area(self):
        """raise error if area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate an integer
        Args:
            name:string
            value: integer to compare with
        Raises:
            TypeError:if its not an integer
            ValueError:if its not greater than zero
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """define geometry operations"""

    def __init__(self, width, height):
        """initialize
        Args:
            width: width of rectangle
            height: heigjt of rectangle
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"
