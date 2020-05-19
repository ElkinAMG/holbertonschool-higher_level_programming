#!/usr/bin/python3
'''This scipt has the complete management over the square class'''


class Square:
    '''This class has the complete management of the object {square}'''

    def __init__(self, size=0, position=(0, 0)):
        '''This function declares a private attribute

        Arguments:
            size {int} → private attribute for the square size (default: 0)
            position {int} → It's a tuple with position in position(x, y)
        '''
        try:
            if size < 0:
                raise ValueError('size must be >= 0')
            self._Square__size = size
        except TypeError:
            raise TypeError('size must be an integer')

        try:
            if position[0] < 0 or position[1] < 0:
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
            self._Square__position = (position[0], position[1])
        except TypeError:
            raise TypeError(
                'position must be a tuple of 2 positive integers')

    @property
    def size(self):
        '''This function returns the square's size.

        Arguments:
                 It has not arguments.
        '''
        return (self._Square__size)

    @size.setter
    def size(self, value):
        '''This function sets the square's size.

        Arguments:
                 value {int} → The value to be setted for square's size.
        '''
        try:
            if value < 0:
                raise ValueError('size must be >= 0')
            self._Square__size = value
        except TypeError:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        '''This function returns the position for printing.

        Arguments:
                 It has not arguments.
        '''
        return (self._Square__position)

    @position.setter
    def position(self, value):
        '''This function sets the position for printing.

        Arguments:
            value {tuple {int, int} } → The value to be setted for position.
        '''
        try:
            if position[0] < 0 or position[1] < 0:
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
            self.Square__position = (position[0], position[1])
        except TypeError:
            raise TypeError(
                'position must be a tuple of 2 positive integers')

    def area(self):
        '''This function return the square's area.

        Arguments:
                 It has not arguments.
        '''
        return (self._Square__size ** 2)

    def my_print(self):
        '''This function prints a square with a given size.

        Arguments:
                 It has not arguments.
        '''
        ar = []
        print('\n' * self.Square__position[1], end="")
        for x in range(self._Square__size):
            ar.append((' ' * self.Square__position[0]) +
                      ('#' * self._Square__size))
        print(*ar, sep="\n")
