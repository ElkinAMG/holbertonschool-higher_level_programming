#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    with get(argv[1]) as res:
        status = res.status_code

        if status >= 400:
            print('Error code:', status)
