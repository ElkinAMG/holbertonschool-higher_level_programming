#!/usr/bin/python3


def search_replace(my_list, search, replace):
    return (list(map(lambda ls: ls if ls != search else replace, my_list)))
