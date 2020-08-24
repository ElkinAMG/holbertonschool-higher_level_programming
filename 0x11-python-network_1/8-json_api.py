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

    if len(user) > 0:
        if 'id' in user and 'name' in user:
            print('[{}] {}'.format(user.get('id'), user.get('name')))
        else:
            print('Not a valid JSON')
    else:
        print('No result')
