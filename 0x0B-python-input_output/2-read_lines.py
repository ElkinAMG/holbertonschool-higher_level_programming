#!/usr/bin/python3
'''

This module has the function `read_lines`.

'''


def read_lines(filename="", nb_lines=0):
    '''
    Reads `nb_lines` lines of `filename`.
    '''

    with open(filename, encoding="UTF-8") as f:

        a = tuple(enumerate(f))
        lines = (a[-1][0] + 1)

        if nb_lines <= 0 or nb_lines >= lines:
            for i in range(lines):
                print(a[i][1], end="")
        else:
            for i in range(nb_lines):
                print(a[i][1], end="")
