#!/usr/bin/python3
"""Define class rectangle"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize rectangle
        Args:
            width:width of rectangle
            height: height of rectangle
         """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get and set width of rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """get and set height of rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """calcuate area"""
        return self.width * self.height

    def perimeter(self):
        """calculate perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self._width + self._height)
