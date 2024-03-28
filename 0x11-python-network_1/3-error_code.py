#!/usr/bin/python3
"""
Take a url and isplay request body
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    try:
        with urllib.request.urlopen(URL) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
