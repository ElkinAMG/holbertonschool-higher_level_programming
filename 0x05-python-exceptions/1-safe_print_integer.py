#!/usr/bin/python3


def safe_print_integer(value):
    bool = True

    try:
        print("{:d}".format(value))
    except ValueError:
        bool = False

    return (bool)
