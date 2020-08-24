#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    import urllib.request as req
    from sys import argv

    url = argv[1]

    try:
        with req.urlopen(url) as res:
            print(res.read().decode())
    except Exception as e:
        print('Error code:', e.status)
