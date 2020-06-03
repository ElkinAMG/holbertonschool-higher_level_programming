#!/usr/bin/python3
'''

This module has the function `read_file`.

'''


def read_file(filename=""):
    '''
    Reads `filename`.
    '''
    with open(filename) as f:
        print(f.read(), end="")
