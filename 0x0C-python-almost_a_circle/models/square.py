#!/usr/bin/python3
"""model to find class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """subclass of rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        slf.y = y

    def __str__(self):
        """human readable string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method to update attributes with *arg and **kwargs"""
        attr = ['id', 'size', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
