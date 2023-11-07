#!/usr/bin/python3
"""define class BaseGeometry"""


class BaseGeometry:
    """do geometry operations"""
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")
 
    def integer_validator(self, name, value):
        """validate integer
        Args:
            name: string
            value: integer
         """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """define rectangle function"""
    def __init__(self, width, height):
        """ initialize
        width: width of rectangle
        height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """defin esquar operations"""
    def __init__(self, size):
        """initialize
        size:size of rectangle
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """informal string representation"""
        return f"[Square] {self.__size}/{self.__size}"
