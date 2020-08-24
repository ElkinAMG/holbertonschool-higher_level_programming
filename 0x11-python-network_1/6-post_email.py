#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    from requests import post
    from sys import argv

    with post(argv[1], data={'email': argv[2]}) as res:
        print(res.text)
