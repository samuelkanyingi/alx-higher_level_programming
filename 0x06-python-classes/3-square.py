#!/usr/bin/python3
""" define a class """


class Square:
    """ define a class properties related on 2-square.py """
    def __init__(self, size=0):
        """
        Args:
        size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns area of square
        """
        return self.__size * self.__size
