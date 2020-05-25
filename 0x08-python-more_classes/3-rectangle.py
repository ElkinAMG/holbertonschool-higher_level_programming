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
        return (self.__width)

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
        return (self.__height)

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

    def area(self):
        '''
        This is the `rectangle`'s area operation.
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''
        This is the `rectangle`'s perimeter operation.
        '''
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        '''
        This function returns a `rectangle`'s graphic.
        '''
        w, h = self.__width, self.__height
        if h > 0 or w > 0:
            return '{}{}'.format(('#' * w + '\n') * (h - 1), '#' * w)
        else:
            return ('')
