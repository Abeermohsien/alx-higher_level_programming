#!/usr/bin/python3
"""
pythons script takes two args
"""
from sys import argv
import requests


if __name__ == "__main__":
    try:
        RepoName = argv[1]
        UserName = argv[2]
        commmitURL = "https://api.github.com/repos/{}/{}/commits" \
            .format(UserName, RepoName)
        response = requests.get(commmitURL)
        jsonObj = response.json()
        for i, j in enumerate(jsonObj):
            if i == 10:
                break
            if type(j) is dict:
                data = j.get('commit').get('author').get('name')
                print("{}: {}".format(j.get('sha'), data))
    except ValueError as invalid_json:
        pass
