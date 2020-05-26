#!/usr/bin/python3
'''
This module contains the class `LockedClass`.
'''


class LockedClass:
    '''
    This class contains nothing.
    '''

    def __setattr__(self, attribute, value):
        '''
        Set dynamically attributes.
        ARGUMENTS:
        → attribute {any type} is the attribute name.
        → value {any type} is the attribute value.
        '''
        if attribute == 'first_name':
            self.__dict__.update({attribute: value})
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(attribute))
