#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    return (list(map(lambda mtx: [i ** 2 for i in mtx], matrix)))
