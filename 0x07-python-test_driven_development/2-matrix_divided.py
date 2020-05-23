#!/usr/bin/python3
'''This module contains the function `matrix_divided` for division.'''


def matrix_divided(matrix, div):
    '''
    This function returns a matrix with element within
    `matrix` divided by `div`.

    ARGUMENTS:

    - matrix {list} is the matrix with integer items.
    - div {int} is the divisor for matrix items.
    '''
    m_error = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list:
        raise TypeError(m_error)

    if any(type(item) != list for item in matrix):
        raise TypeError(m_error)

    if any(type(y) not in [int, float] for x in matrix for y in x):
        raise TypeError(m_error)

    ln = list([len(x) for x in matrix])
    if any(i != ln[0] for i in ln):
        raise TypeError('Each row of the matrix must have the same size')

    if type(div) not in set([int, float]):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return (list(map(lambda x: list(map(lambda y:
                                        round(y / div, 2), x)), matrix)))
