#!/usr/bin/python3
'''

This module has the function `inherits_from`.

'''


def inherits_from(obj, a_class):
    '''
    This function checks whether or not
    `obj` is an instance of a class that
    inherited from the specified class.

    ARGUMENTS:
    → obj {object}.
    → a_class {class}.
    '''

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
