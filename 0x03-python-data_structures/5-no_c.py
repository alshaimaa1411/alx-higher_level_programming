#!/usr/bin/python3
def no_c(my_string):
    n_string = ""
    x = len(my_string) - 1
    for i in range(0, x):
        if 'c' == my_string[i] or 'C' == my_string[i]:
            continue
        else:
            n_string += my_string[i]
    return n_string
