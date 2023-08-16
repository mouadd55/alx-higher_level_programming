#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for item in my_list:
        if item == search:
            new_list[item] = replace
    return new_list
