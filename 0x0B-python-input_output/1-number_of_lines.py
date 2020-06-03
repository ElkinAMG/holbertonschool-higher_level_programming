#!/usr/bin/python3
'''

This module has `number_of_lines`.

'''


def number_of_lines(filename=""):
    '''
    Returns the number of lines of `filename`.
    '''

    with open(filename, encoding="UTF-8") as f:
        count = 0
        for i in f:
            count += 1
        return (count)
