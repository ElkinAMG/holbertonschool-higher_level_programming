#!/usr/bin/python3


def safe_print_integer(value):
    try:
        bool = True
        print("{:d}".format(value))
    except ValueError:
        bool = False
    return (bool)
