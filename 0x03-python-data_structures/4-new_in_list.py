#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = len(my_list) - 1
    n_list = []
    n_list += my_list
    if idx < 0:
        return my_list
    elif idx > x:
        return my_list
    else:
        n_list[idx] = element
        return n_list
