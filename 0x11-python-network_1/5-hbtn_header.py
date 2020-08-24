#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    with get(argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
