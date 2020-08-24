#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    import urllib.request as req

    url = 'https://intranet.hbtn.io/status'

    with req.urlopen(url) as res:
        fetched = res.read()

        prompt = 'Body response:\
\n\t- type: {}\
\n\t- content: {}\
\n\t- utf8 content: {}'

        print(prompt.format(type(fetched), fetched, fetched.decode()))
