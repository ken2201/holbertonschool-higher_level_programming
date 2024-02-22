#!/usr/bin/python3
"""Module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Overriding constructor from Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square"""
        return '[Square] ({}) {}/{} - {}' \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set value to size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square with keyword_argument"""
        attributes = ['id', 'size', 'x', 'y']

        for idx, x in enumerate(args):
            if idx >= len(attributes):
                return

            self.__setattr__(attributes[idx], x)

        if args:
            return

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        list_atr = ['id', 'size', 'x', 'y']
        dict_rep = {}

        for key in list_atr:
            if key == 'size':
                dict_rep[key] = getattr(self, 'width')
            else:
                dict_rep[key] = getattr(self, key)
        return dict_rep
