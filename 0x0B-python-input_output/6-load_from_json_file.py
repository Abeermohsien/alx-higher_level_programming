#!/usr/bin/python3
"""load from json"""


import json


def save_to_json_file(my_obj, filename):
    """save to json"""
    with open(filename, "r", encoding="utf-8") as filee:
        return json.load(filee)
