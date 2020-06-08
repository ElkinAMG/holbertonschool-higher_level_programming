#!/usr/bin/python3
'''

This file has the `Rectangle` class.

'''
from .base import Base


class Rectangle(Base):
    '''
    This is the template for `Rectangle` objects.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        The init constructor for:
             → `width` for `Rectangle`.
             → `height` for `Rectangle`.
             → `x` for `Rectangle`.
             → `y` for `Rectangle`.
        '''

        self.catch_wh("width", width)
        self.catch_wh("height", height)

        self.__width = width
        self.__height = height

        self.catch_xy("x", x)
        self.catch_xy("y", y)

        self.__x = x
        self.__y = y
        super().__init__(id)

    def catch_wh(self, typ="", value=0):
        '''
        Catch errors W-H.
        '''

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(typ))
        if value <= 0:
            raise ValueError("{} must be > 0".format(typ))

    def catch_xy(self, typ="", value=0):
        '''
        Catch errors X-Y.
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(typ))
        if value < 0:
            raise ValueError("{} must be >= 0".format(typ))

    @property
    def width(self):
        '''
        It returns the current `Rectangle's width`.
        '''

        return (self.__width)

    @width.setter
    def width(self, value):
        '''
        Sets the `Rectangle's width`.
        '''
        self.catch_wh("width", value)

        self.__width = value

    @property
    def height(self):
        '''
        Returns the `Rectangle's height`.
        '''

        return (self.__height)

    @height.setter
    def height(self, value):
        '''
        Sets the `Rectangle's height`.
        '''
        self.catch_wh("height", value)

        self.__height = value

    @property
    def x(self):
        '''
        Returns the `x` value.
        '''

        return (self.__x)

    @x.setter
    def x(self, value):
        '''
        Sets the `x` value.
        '''
        self.catch_xy("x", value)

        self.__x = value

    @property
    def y(self):
        '''
        Returns the `y` value.
        '''

        return (self.__y)

    @y.setter
    def y(self, value):
        '''
        Sets the `y` value.
        '''
        self.catch_xy("y", value)

        self.__y = value

    def area(self):
        '''
        Returns the area of `Rectangle`.
        '''

        return (self.__width * self.__height)

    def display(self):
        '''
        Prints `Rectangle` instance.
        '''

        print('\n' * self.__y, end="")

        for i in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        '''
        Returns `Rectangle` description.
        '''

        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        '''
        Updates `Rectangle`.
        '''

        if len(args):
            for a, b in enumerate(args):
                if a == 0:
                    self.id = b
                if a == 1:
                    self.catch_wh("width", b)
                    self.__width = b
                if a == 2:
                    self.catch_wh("height", b)
                    self.__height = b
                if a == 3:
                    self.catch_xy("x", b)
                    self.__x = b
                if a == 4:
                    self.catch_xy("y", b)
                    self.__y = b
        else:
            for a, b in kwargs.items():
                if a in "id":
                    self.id = b
                elif a in "width":
                    self.catch_wh("width", b)
                    self.__width = b
                elif a in "height":
                    self.catch_wh("height", b)
                    self.__height = b
                elif a in "x":
                    self.catch_xy("x", b)
                    self.__x = b
                elif a in "y":
                    self.catch_xy("y", b)
                    self.__y = b

    def to_dictionary(self):
        '''
        Returns the dictionary representation of `Rectangle`.
        '''

        dicti = {}

        dicti['id'] = self.id
        dicti['width'] = self.width
        dicti['height'] = self.height
        dicti['x'] = self.x
        dicti['y'] = self.y

        return (dicti)
