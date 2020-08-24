#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    import urllib.request as req
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    data = urlencode({'email': argv[2]})
    data = data.encode('ascii')

    with req.urlopen(url, data) as res:
        print(res.read().decode())
