#!/usr/bin/python3
"""define a class"""


class Square:
    """define a class properties based on 3-square.py"""
    def __init__(self, size=0):
        """
        args:
        size: size of square
        """
        self.size = size

    @property
    def size(self):
        """return size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of square"""
        return self.__size * self.__size
