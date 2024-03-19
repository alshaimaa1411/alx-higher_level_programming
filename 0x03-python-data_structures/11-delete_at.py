#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list):
        return my_list
    else:
        for i in range(0, len(my_list) - 1):
            if i != my_list[idx]:
                n_list += i
            else:
                continoues
        return n_list
