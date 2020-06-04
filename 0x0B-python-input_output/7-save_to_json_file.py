#!/usr/bin/python3
'''

This module has `save_to_json_file`.

'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Writes an Object to `filename`, using JSON.
    '''

    with open(filename) as f:
        json.dump(my_obj, f)
