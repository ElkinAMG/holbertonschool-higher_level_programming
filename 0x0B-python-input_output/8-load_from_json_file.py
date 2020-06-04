#!/usr/bin/python3
'''

This module has `load_from_json_file`.

'''
import json


def load_from_json_file(filename):
    '''
    Creates an Object from `filename`.
    '''

    with open(filename) as f:
        obj = json.load(f)

    return (obj)
