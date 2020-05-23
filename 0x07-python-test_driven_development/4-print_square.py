#!/usr/bin/python3
'''

This module contains the function `print_square` for print a square.

'''


def print_square(size):
    '''This function prints a square.
    - size {int/float} is the `size` of the square'''
    if type(size) not in set([int, float]):
        raise TypeError('size must be an integer')
    if size < 0:
        if type(size) is float:
            raise TypeError('size must be an integer')
        raise ValueError('size must be >= 0')
    size = int(size)
    if size > 0:
        print(*['#'*size for x in range(size)], sep="\n")
