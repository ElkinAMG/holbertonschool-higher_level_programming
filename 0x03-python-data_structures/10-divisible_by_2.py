#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = []

    for tripper in my_list:
        new_list.append(True) if tripper % 2 == 0 else new_list.append(False)
    return (new_list)
