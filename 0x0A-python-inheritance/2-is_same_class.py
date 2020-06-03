#!/usr/bin/python3
'''

This module has the function `is_same_class`
for find out if an object is an instance of
a specific class.

'''


def is_same_class(obj, a_class):
    '''
    This function find out if `obj` is
    an instance of `a_class`.

    ARGUMENTS:
    → obj {object}.
    → a_class {class}.
    '''

    return (type(obj) == a_class)
