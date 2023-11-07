#!/usr/bin/python3
"""define class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define subclass rectangle"""

    def __init__(self, width, height):
        """initialize rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
