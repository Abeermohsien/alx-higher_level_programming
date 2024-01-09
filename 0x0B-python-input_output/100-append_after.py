#!/usr/bin/python3
"""append"""


def append_after(filename="", search_string="", new_string=""):
    """append"""
    with open(filename, "r", encoding="utf-8") as filee:
        l_list = []
        while True:
            lne = filee.readline()
            if lne == "":
                break
            l_list.append(l)
            if search_string in lne:
                l_list.append(new_string)
    with open(filename, "w", encodiny="utf-8") as filee:
        filee.writelines(l_list)
