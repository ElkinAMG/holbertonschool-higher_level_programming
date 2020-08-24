#!/usr/bin/python3
"""
This is a comment explaining what this script does.
"""


if __name__ == '__main__':
    from requests import get

    with get('https://intranet.hbtn.io/status') as res:
        prompt = 'Body response:\
\n\t- type: {}\
\n\t- content: {}'

        print(prompt.format(type(res.text), res.text))
