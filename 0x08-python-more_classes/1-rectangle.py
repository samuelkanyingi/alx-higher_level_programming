#!/usr/bin/python3
"""define class Rectangle"""


class Rectangle:
    """define attributes of rectangle"""
    def __init__(self, width=0, height=0):
        """initialize Rectangle object
        Args:
            width:width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of rectangle
        returns:
            width of rectangle
        """
        return self.__width

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
            self.__width = value

    @property
    def height(self):
        """get height of rectangle
        Returns:
            height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle
        Args:
            height of rectangle
        value:
            height of rectangle
        Raises:
            Typeerror:If value is not an integer
             ValueError: if value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
