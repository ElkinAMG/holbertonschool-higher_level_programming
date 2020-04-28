#!/usr/bin/python3
def islower(c):
    for check in range(ord("a"), ord("z") + 1):
        if check == ord(c):
            return True
    return False
