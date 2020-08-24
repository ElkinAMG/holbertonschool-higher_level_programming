#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    from requests import post
    from sys import argv

    res = post(argv[1], data={'email': argv[2]})
    print(res.text)
