#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx in range(len(my_list)):
        val = my_list[idx]
        my_list.remove(val)
    return (my_list)
