#!/usr/bin/python3
"""
Takes a URL and send a request to it and display a variable value
"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        info = response.info()
        val = info.get('X-Request-Id')
        print(val)
