#!/usr/bin/python3
'''

This module contains the function `add_integer` for addition.

'''


def add_integer(a, b=98):
    '''This function returns the addition of a and b.
    - a {int} is the first parameter to add.
    - b {int} is the second parameter to add. [default: 98]'''
    if type(a) not in set([int, float]):
        raise TypeError('a must be an integer')
    if type(b) not in set([int, float]):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
