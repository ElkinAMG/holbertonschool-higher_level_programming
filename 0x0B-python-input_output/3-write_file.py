#!/usr/bin/python3
'''

This module has `write_file`.

'''


def write_file(filename="", text=""):
    '''
    Writes `text` to `filename`.
    '''

    with open(filename, "w", encoding="UTF-8") as f:
        lines = f.write(text)
        return (lines)
