#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda n: replace if e == search else e, my_list))
