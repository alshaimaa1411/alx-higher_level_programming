#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = []
    for i in my_list:
        if i !=  search:
            n_list.append(i)
        else:
            n_list.append(replace)
    return n_list
