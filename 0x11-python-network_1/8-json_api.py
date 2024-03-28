#!/usr/bin/python3
"""
send a post request
"""
from sys import argv
import requests


if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    para = {"q": q}
    response = requests.post(URL, data=para)
    try:
        jsonOutPut = response.json()
        if not jsonOutPut:
            print("No result")
        else:
            MyId = jsonOutPut.get("id")
            MyName = jsonOutPut.get("name")
            print("[{}] {}".format(MyId, MyName))
    except ValueError as invalid_json:
        print("Not a valid JSON")
