#!/usr/bin/python3
'''

This module has in it the class `Rectangle`.

'''


class Rectangle:
    '''
    Thiss class defines a rectangle.
    '''

    def __init__(self, width=0, height=0):
        '''
        This is the initialize constructor for `rectangle`

        ARGUMENTS:

        → width {int} is the width of the `rectangle`. [deafult: 0]
        → height {int} is the height of the `rectangle`. [deafult: 0]
        '''
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def width(self):
        '''
        This is the width getter of `rectangle`.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        This is the width setter of `rectangle`.

        ARGUMENTS:
        → value {int} is the width value for the `rectangle`
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''
        This is the height getter of `rectangle`.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        This is the height setter of `rectangle`.

        ARGUMENTS:
        → value {int} is the height value for the `rectangle`
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
