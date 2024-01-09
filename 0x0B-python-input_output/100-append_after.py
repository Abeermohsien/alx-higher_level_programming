#!/usr/bin/python3
"""append"""


def append_after(filename="", search_string="", new_string=""):
    """append"""
    with open(filename, "r", encoding="utf-8") as filee:
        l_list = []
        while True:
            l = filee.readline()
            if l == "":
                break
            l_list.append(l)
            if search_string in l:
                l_list.append(new_string)
    with open(filename, "w", encodiny="utf-8") as filee:
        filee.writelines(line_list)
