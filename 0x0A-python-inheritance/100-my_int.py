#!/usr/bin/python3
'''

This module has the class `MyInt`.

'''


class MyInt(int):
    '''
    This class reverses `==` and `!=` operators.
    '''

    def __eq__(self, num):
        '''
        `!=` operator.
        '''
        return (True if num != self.__int__() else False)

    def __ne__(self, num):
        '''
        `==` operator.
        '''
        return (True if num == self.__int__() else False)
