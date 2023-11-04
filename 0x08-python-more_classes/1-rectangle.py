#!/usr/bin/python3
"""Define class rectangle"""


class Rectangle:
    """define class rectangle"""

    def __init__(self, width=0, height=0):
        """initialize rectangle.
        width(int): width of rectangle
        height(int: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get and set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """get and set height of rectangle"""
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
