#!/usr/bin/python3
"""
Script to send post requewt
"""
import requests
from sys import argv


if __name__ == "__main__":
    URL = argv[1]
    Email = argv[2]
    para = {
        "email": Email
    }
    response = requests.post(URL, data=para)
    print(response.text)
