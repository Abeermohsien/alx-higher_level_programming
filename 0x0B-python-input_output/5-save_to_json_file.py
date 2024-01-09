#!/usr/bin/python3
"""sve to json"""


import json


def save_to_json_file(my_obj, filename):
    """save json"""
    with open(filename, "w", encoding="utf-8") as filee:
        json.dump(my_obj, filee)
