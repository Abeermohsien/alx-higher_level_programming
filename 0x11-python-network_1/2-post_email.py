#!/usr/bin/python3
"""
Takes a url and email as parameter
"""
import urllib.parse as parse
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    URL = argv[1]
    Email = argv[2]
    AsAPara = {
        "email": Email
    }
    QueryString = parse.urlencode(AsAPara)
    MailData = QueryString.encode("ascii")
    Req = request.Request(URL, MailData)
    with request.urlopen(Req) as response:
        print(response.read().decode("utf-8"))
