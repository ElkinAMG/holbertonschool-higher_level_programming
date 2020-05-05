#!/usr/bin/python3


def check(tup, pos):
    try:
        return(tup[pos])
    except IndexError:
        return (0)


def add_tuple(tuple_a=(), tuple_b=()):
    t_a = (check(tuple_a, 0) + check(tuple_b, 0))
    t_b = (check(tuple_a, 1) + check(tuple_b, 1))
    return (t_a, t_b)
