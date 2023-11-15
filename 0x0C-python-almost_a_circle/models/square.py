#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """intialize square
        Args:
            size: length of each side of rectangle
            x: return x cordinate of rectangle
            y: return y cordinate of rectangle
            id: identifier of rectangle
        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter
        Args:
            Value: The new length value
        Return:
            None
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes with no-keyword and kwargs
        Args:
            *args: Positional arguments to show attributes
            **kwargs: Keyword arguments to show attributes
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(min(len(args), len(attributes))):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def __str__(self):
        """String representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
