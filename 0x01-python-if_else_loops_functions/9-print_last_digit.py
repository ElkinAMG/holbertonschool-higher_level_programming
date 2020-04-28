#!/usr/bin/python3


def print_last_digit(number):
    last_stone = (number % 10)
    print("{:d}".format(last_stone), end="")
    return last_stone
