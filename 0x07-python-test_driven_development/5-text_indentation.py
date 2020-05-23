#!/usr/bin/python3
'''

This module contains the function `text_indentation`
for printing with indentation.

'''


def text_indentation(text):
    '''This function prints with indentation.
    - text {str} will be printed with indentations'''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    new_str = "".join([x if x not in ".?:" else x + "\n\n" for x in text])
    print("\n".join([x.strip() for x in new_str.split("\n")]), end="")
