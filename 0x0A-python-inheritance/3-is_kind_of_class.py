#!/usr/bin/python3
'''

This module has the function `is_kind_of_class`
for check if an object is an instance of another
of came from it.

'''


def is_kind_of_class(obj, a_class):
    '''
    This function checks if `obj` is an instance
    of a_class or came from it.

    ARGUMENTS:
    → obj {object}.
    → a_class {class}.
    '''

    return (isinstance(obj, a_class))
