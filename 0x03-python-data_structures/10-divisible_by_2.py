#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    dilist = []
    for j in my_list:
        if (j % 2) == 0:
            dilist.append(True)
        else:
            dilist.append(False)
    return dilist
