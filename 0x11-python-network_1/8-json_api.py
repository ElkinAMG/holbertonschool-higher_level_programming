#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    from requests import post
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'

    query = argv[1] if len(argv) > 1 else ""

    res = post(url, data={'q': query})
    user = res.json()

    if not type(user) is dict:
        print('Not a valid JSON')

    if len(user) > 0:
        print('[{}] {}'.format(user.get('id'), user.get('name')))
    else:
        print('No result')
