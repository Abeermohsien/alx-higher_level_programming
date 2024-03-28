#!/usr/bin/python3
"""
python script to fetch
"""
from requests import get


if __name__ == "__main__":
    URL = "https://alx-intranet.hbtn.io/status"
    response = get(URL)
    BytesContent = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(BytesContent)))
    print('\t- content: {}'.format(BytesContent))
