#!/usr/bin/python3
'''
This module contains the class `LockedClass`.
'''


class LockedClass:
    def __setattr__(self, key, value):
        '''
        Set dynamically attributes.
        ARGUMENTS:
        → key {any type} is the attribute name.
        → value {any type} is the attribute value.
        '''
        if key == 'first_name':
            self.__dict__.update({key: value})
        else:
            raise AttributeError("{} object has no attribute '{}'".format(
                __class__.__name__, key))
