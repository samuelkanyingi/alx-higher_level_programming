#!/usr/bin/python3
"""a class that define Rectangle"""


class Rectangle:
    """define attributes of a class"""

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
        """get or set width of rectangle"""
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
        return: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle
        Args:
            value:height of rectangle
        Raises:
             Typeerror: if height is not int
             ValueError: height less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculate area"""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter"""
        return 2 * (
                 self.__width + self.__height
                  ) if self.__width > 0 and self.__height > 0 else 0

    def __str__(self):
        """output informal string representation using '#' character"""
        res = ""
        for i in range(self.__height):
            res += "#" * self.__width + "\n"
        return res[:-1]

    def __repr__(self):
        """"output formal string representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
