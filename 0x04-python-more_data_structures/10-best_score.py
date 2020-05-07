#!/usr/bin/python3


def best_score(a_dictionary):
    w_name = None
    if a_dictionary:
        w_value = 0
        for i, j in a_dictionary.items():
            if j > w_value:
                w_value = j
                w_name = i
    return (w_name)
