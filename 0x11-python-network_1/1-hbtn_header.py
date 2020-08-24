#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    import urllib.request as req
    from sys import argv

    url = argv[1]

    with req.urlopen(url) as res:
        req_id = res.getheader('X-Request-Id')
        print(req_id)
