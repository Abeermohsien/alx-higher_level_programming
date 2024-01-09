#!/usr/bin/python3
"""save to json"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

argl = list(sys.argv[1:])

try:
    o_data = load_from_json_file("add_item.json")
except Exception:
    o_data = []

o_data.extend(argl)
save_to_json_file(o_data, "add_item.json")
