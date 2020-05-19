#!/usr/bin/python3
'''This scipt has the complete management over the square class'''


class Square:
    '''This class has the complete management of the object {square}'''

    def __init__(self, size=0):
        '''This function declares a private attribute

        Arguments:
            size {int} → private attribute for the square size (default: 0)
        '''
        try:
            if size < 0:
                raise ValueError('size must be >= 0')
            self._Square__size = size
        except TypeError:
            raise TypeError('size must be an integer')

    def area(self):
        '''This function return the square's area.

        Arguments:
                 It has not arguments.
        '''
        return (self._Square__size ** 2)
