#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    rt = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            rt = rt + 1
        except:
            pass
    print('')
    return (rt)
