#!/usr/bin/python3
'''

This modules has `Student` class.

'''


class Student:
    '''
    Defines a student.
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Initial constructor.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Retrieves a dictionary representation of a `Student`
        '''
        attr = {}
        if attrs is not None:
            for i in attrs:
                if hasattr(self, i):
                    attr[i] = getattr(self, i)
        else:
            return (self.__dict__)
        return (attr)
