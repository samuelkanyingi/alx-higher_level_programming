#!/usr/bin/python3
"""a class that define Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """initialize Rectangle object
        Args:
            width:width of rectangle
            height: height of rectangle
        """
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """get or set width of rectangle
       raises:
           Typeerror: if width is not int
           ValueError: width less than 0
        """
        return self._width

    @width.setter
    def width(self, value):
        """set width of rectangle
        Args:
            value:width of rectangle
        Raises:
             Typeerror: if width is not int
             ValueError: width less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """get or set height of rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """set height of rectangle
        Args:
            height of rectangle
        value:height of rectangle
        Raises:
            Typeerror:If value is not an integer
             ValueError: if value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
