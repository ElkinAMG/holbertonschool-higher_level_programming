#!/usr/bin/python3
'''

This file has the class `Square`.

'''
from .rectangle import Rectangle


class Square(Rectangle):
    '''
    This class inherits from `Rectangle`.
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        This constructor defines features for `Square`.
        '''

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''
        Returns the size.
        '''

        return (self.width)

    @size.setter
    def size(self, value):
        '''
        Sets the size.
        '''

        self.width = value
        self.height = value

    def __str__(self):
        '''
        Shows Square's features.
        '''

        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.width))

    def update(self, *args, **kwargs):
        '''
        Updates `Square`.
        '''

        if len(args):
            for a, b in enumerate(args):
                if a == 0:
                    self.id = b
                elif a == 1:
                    self.size = b
                elif a == 2:
                    self.x = b
                elif a == 3:
                    self.y = b
        else:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "size" in kwargs:
                self.size = kwargs['size']
            if "x" in kwargs:
                self.x = kwargs['x']
            if "y" in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        '''
        Returns the dictionary representation of `Square`.
        '''

        d = {}

        d['id'] = self.id
        d['size'] = self.size
        d['x'] = self.x
        d['y'] = self.y

        return (d)
