#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    return (dict(map(lambda age: [x*2 for x in age], a_dictionary.items())))
