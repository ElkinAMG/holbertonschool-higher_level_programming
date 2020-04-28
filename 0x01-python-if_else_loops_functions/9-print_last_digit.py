#!/usr/bin/python3


def print_last_digit(number):
    last_stone = abs(number) % 10
    print(last_stone, end="")
    return last_stone
