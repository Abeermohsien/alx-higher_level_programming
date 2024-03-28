#!/usr/bin/python3
"""
pythons script to diplay body
"""
from sys import argv
import requests


if __name__ == "__main__":
    URL = argv[1]
    data = requests.get(URL)
    RequestBody = data.text
    if data.status_code >= 400:
        print("Error code: {}".format(data.status_code))
    else:
        print(RequestBody)
