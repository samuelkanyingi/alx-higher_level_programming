#!/usr/bin/python3
"""define class BaseGeometry"""


class BaseGeometry:
    """peform geometry operatisn"""
    def area(self):
        """function not implemnted"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to check for validation
        Args:
            name:string
            value:integer
        Raises:
            TypeError: if name not an integer
            ValueError: if number not greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """function  to do geometry operation"""
    def __init__(self, width, height):
        """initialize
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """function to calculate area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """performs square operations"""
    def __init__(self, size):
        """function that perform square operation"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """informal string representation"""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
