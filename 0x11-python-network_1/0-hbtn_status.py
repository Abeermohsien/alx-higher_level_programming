#!/usr/bin/python3
"""Fetch URL using urlopen"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        print('Body response:')
        print('\t- type: {}'.format(type(response.read())))
        print('\t- content: {}'.format(response.read()))
        print('\t- utf8 content: {}'.format(response.read().decode("utf-8")))
