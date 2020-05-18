#!/usr/bin/python3


def safe_print_integer(value):
    bool = True

    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        bool = False

    return (bool)
