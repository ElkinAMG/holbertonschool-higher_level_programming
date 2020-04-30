#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = (len(argv) - 1)

    print("{:d} {:s}".format(args, "arguments:" if args > 1 else
                             "arguments." if args == 0 else "argument:"))

    for index, tripper in enumerate(argv[1:]):
        print("{:d}: {:s}".format((index + 1), tripper))
