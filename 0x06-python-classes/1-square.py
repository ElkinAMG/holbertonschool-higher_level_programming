#!/usr/bin/python3
'''This script declares a class with a function that declares a
private attribute'''


class Square:
    '''This class declares a function that declares a private attribute'''

    def __init__(self, size):
        '''This function declares a private attribute

        Arguments:
            size {int} → private attribute for the square size (default: 0)
        '''
        self._Square__size = size
