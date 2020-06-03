#!/usr/bin/python3
'''

This module has `to_json_string`.

'''
import json


def to_json_string(my_obj):
    '''
    Returns the JSON representation of `my_obj`.
    '''
    return (json.dumps(my_obj))
