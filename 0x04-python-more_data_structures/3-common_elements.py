#!/usr/bin/python3
def common_elements(set_1, set_2):
    n_set = []
    for i in set_1:
        for a in set_2:
            if i == a:
                n_set.append(i)
    return n_set
