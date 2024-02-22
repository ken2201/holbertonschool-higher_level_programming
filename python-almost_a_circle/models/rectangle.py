#!/usr/bin/python3
"""module for rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    Class that represents a Rectangle and inherits from Base.

    Private instance attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
        __x (int): x-coordinate of the rectangle
        __y (int): y-coordinate of the rectangle

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): id of the rectangle. Defaults to None.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): new value for the width attribute.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): new value for the height attribute.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
            int: x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): new value for the x attribute.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
            int: y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays a rectangle using # to stdout"""
        w, h = self.width, self.height
        x, y = self.x, self.y

        print('\n' * y, end='')
        pattern = '{}' \
            .format((' ' * x + '#' * w + '\n') * self.__height)
        print(pattern, end='')

    def __str__(self):
        """Overriding str method from Base"""
        return '[Rectangle] ({}) {}/{} - {}/{}' \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the object with keyword-argument"""
        attributes = ['id', 'width', 'height', 'x', 'y']

        for idx, x in enumerate(args):
            if idx >= len(attributes):
                return

            self.__setattr__(attributes[idx], x)

        if args:
            return

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_rep = {}

        for key in list_atr:
            dict_rep[key] = getattr(self, key)
        return dict_rep
