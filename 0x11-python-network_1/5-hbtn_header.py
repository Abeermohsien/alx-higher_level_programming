#!/usr/bin/python3
"""
script to takes a url and then dispalys a var value
"""
from requests import get
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    response = get(URL)
    print(response.headers.get("X-Request-Id"))
