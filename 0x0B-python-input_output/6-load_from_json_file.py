#!/usr/bin/python3
"""load from json"""


import json


def load_from_json_file(filename):
    """save to json"""
    with open(filename, "r", encoding="utf-8") as filee:
        return json.load(filee)
