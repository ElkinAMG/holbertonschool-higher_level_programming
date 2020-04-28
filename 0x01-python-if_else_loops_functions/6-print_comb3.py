#!/usr/bin/python3
for head in range(10):
    for track in range(1, 10):
        if head == 0:
            print("{:02d}".format(track), end=", ")
        elif head > 0 and track < (10 - head):
            if head < 8:
                print("{:02d}".format((track + head) + (head * 10)), end=", ")
            else:
                print("{:02d}".format((track + head) + (head * 10)))
