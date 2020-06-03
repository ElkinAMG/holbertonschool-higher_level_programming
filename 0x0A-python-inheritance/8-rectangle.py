#!/usr/bin/python3
'''

This file contains a class called `BaseGeometry`.

'''


class BaseGeometry:
    '''
    This is a class for make Geometry Operations.
    '''

    def area(self):
        '''
        This function raise an error.
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        This function validates if value accomplish the
        required checks.
        '''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''
    This is a rectangle.
    '''

    def __init__(self, width, height):
        '''
        This is the initialization constructor.
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
