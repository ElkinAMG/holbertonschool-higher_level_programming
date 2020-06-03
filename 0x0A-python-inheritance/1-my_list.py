#!/usr/bin/python3
'''

This module has a class `MyList` that
inherits from `list`.

'''


class MyList(list):
    '''
    This class has the method `print_sorted`.
    '''

    def print_sorted(self):
        '''
        This function prints in sorted way the list.
        '''
        print(sorted(self))
