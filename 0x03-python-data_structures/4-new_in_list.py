#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return my_list

    copy_my_list = my_list.copy()
    copy_my_list[idx] = element
    return copy_my_list
