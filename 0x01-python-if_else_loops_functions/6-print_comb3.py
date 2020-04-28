#!/usr/bin/python3
for head in range(10):
    for track in range(1, 10):
        if track < (10 - head):
            print("{:02d}".format((track + head) + (head * 10)),
                  end=", " if head < 8 else '\n')
