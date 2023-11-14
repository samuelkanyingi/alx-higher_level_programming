#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """intializee square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes with no-keyword and kwargs"""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(min(len(args), len(attributes))):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def __str__(self):
        """String representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
