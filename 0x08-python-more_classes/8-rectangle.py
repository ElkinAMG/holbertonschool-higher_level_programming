#!/usr/bin/python3
'''

This module has in it the class `Rectangle`.

'''


class Rectangle:
    '''
    Thiss class defines a rectangle.
    '''

    number_of_instances = 0
    print_symbol = '#'

    @staticmethod
    def increment():
        '''
        It increments the instances.
        '''
        Rectangle.number_of_instances += 1

    @staticmethod
    def decrement():
        '''
        It decrements the instances.
        '''
        Rectangle.number_of_instances -= 1

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

        self.increment()

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
        grp = str(self.print_symbol)
        if h > 0 or w > 0:
            return '{}{}'.format((grp * w + '\n') * (h - 1), grp * w)
        else:
            return ('')

    def __repr__(self):
        '''
        This function returns a `rectangle`'s graphic.
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''
        This function returns message on deleting `rectangle`.
        '''
        self.decrement()
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        This function returns the `Rectangle` instance with bigger area.

        ARGUMENTS:
        → rect_1 {Rectangle} is an instance of `Rectangle`.
        → rect_2 {Rectangle} is an instance of `Rectangle`.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        r1, r2 = rect_1.area(), rect_2.area()
        if r1 > r2:
            return (rect_1)
        elif r2 > r1:
            return (rect_2)
        else:
            return (rect_1)
