#!/usr/bin/python3
"""
github api
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    URL = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    response = requests.get(URL, auth=HTTPBasicAuth(username, password))
    JsonObj = response.json()
    print(JsonObj.get("id"))
