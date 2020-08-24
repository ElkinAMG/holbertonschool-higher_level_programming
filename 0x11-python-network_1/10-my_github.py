#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    url = 'https://api.github.com/user'

    res = get(url, auth=(argv[1], argv[2]))
    user = res.json()

    print(user.get('id'))
