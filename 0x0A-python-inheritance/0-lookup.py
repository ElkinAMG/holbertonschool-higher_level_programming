#!/usr/bin/python3
"""

This module has the function `lookup` that
returns a list with attributes
and methods of an object.

"""


def lookup(obj):
    '''
    This function returns a list with
    attributes and methods of `obj`.

    ARGUMENTS:
    → obj {obj} is an object.
    '''

    return (dir(obj))
