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
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = size

        if type(position[0]) != tuple or type(position[1]) != tuple:
            raise TypeError(
                'position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError(
                'position must be a tuple of 2 positive integers')
        self.position = (position[0], position[1])

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
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = size

    @property
    def position(self):
        '''This function returns the position for printing.

        Arguments:
                 It has not arguments.
        '''
        return (self.position)

    @position.setter
    def position(self, value):
        '''This function sets the position for printing.

        Arguments:
            value {tuple {int, int} } → The value to be setted for position.
        '''
        if type(position[0]) != tuple or type(position[1]) != tuple:
            raise TypeError(
                'position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError(
                'position must be a tuple of 2 positive integers')
        self.position = (position[0], position[1])

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
        print('\n' * self.position[1], end="")
        for x in range(self._Square__size):
            ar.append((' ' * self.Square__position[0]) +
                      ('#' * self._Square__size))
        print(*ar, sep="\n")