#!/usr/bin/python3
"""Defines class square"""


class Square:
    """Defines class square properties"""
    def __init__(self, size=0):
        """size: size of square(default = 0)
        __size:private size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
