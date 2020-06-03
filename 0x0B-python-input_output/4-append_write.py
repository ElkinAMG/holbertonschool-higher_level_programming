#!/usr/bin/python3
'''

This module has `append_write`.

'''


def append_write(filename="", text=""):
    '''
    Appends `text` at the end of `filename`.
    '''

    with open(filename, 'a', encoding="UTF-8") as f:
        char = f.write(text)
        return (char)
