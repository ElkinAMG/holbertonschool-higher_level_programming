#!/usr/bin/python3
'''

This module has the function `read_lines`.

'''


def read_lines(filename="", nb_lines=0, encoding="UTF-8"):
    '''
    Reads `nb_lines` lines of `filename`.
    '''

    with open(filename) as f:
        a = tuple(enumerate(f))
        if nb_lines <= 0 or nb_lines >= (a[-1][0] + 1):
            for i in range(a[-1][0] + 1):
                print(a[i][1], end="")
        else:
            for i in range(nb_lines):
                print(a[i][1], end="")
