#!/usr/bin/python3
"""define class rectangle"""
from models.base import Base


class Rectangle(Base):
    """rectangle inherits base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height  must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def display(self):
        """print rectangle with #"""
        r = 0
        while r < self.__y:
            print()
            r += 1
        r = 0
        while r < self.__height:
            print(" " * self.__x + "#" * self.__width)
            r += 1

    def to_dictionary(self):
        return {'id': self.id,
                'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def __str__(self):
        """override str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """"update attribute"""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(min(len(args), len(attributes))):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
