#!/usr/bin/python3
def no_c(my_string):
    n_string = ""
    for i in my_string:
        if 'c' == i or 'C' == i:
            continue
        else:
            n_string += i
    return n_string
