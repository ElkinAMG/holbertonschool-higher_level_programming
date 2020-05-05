#!/usr/bin/python3


def no_c(my_string):
    new_string = ''.join([my_string[i]
                          for i in range(len(my_string))
                          if my_string[i] not in "Cc"])
    return (new_string)
