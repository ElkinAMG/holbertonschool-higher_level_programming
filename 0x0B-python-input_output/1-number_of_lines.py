#!/usr/bin/python3
'''

This module has `number_of_lines`.

'''


def number_of_lines(filename=""):
    '''
    Returns the number of lines of `filename`.
    '''

    with open(filename) as f:
        for x, i in enumerate(f):
            pass
        return (x)
