#!/usr/bin/python3
'''

This module contains the function `say_my_name` for showing.

'''


def say_my_name(first_name, last_name=""):
    '''This function prints a message.
    - first_name {str} is the first name.
    - last_name {str} is the last name. [default: <BLANK>]'''
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
