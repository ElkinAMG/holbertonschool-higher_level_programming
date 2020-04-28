#!/usr/bin/python3

def islower(c):
    return ord(c) > 96 and ord(c) < 123

def uppercase(str):
    for tripper in str:
        print("{:c}".format(
            ord(tripper) - 32 if islower(tripper) else ord(tripper)), end="")
    print()
