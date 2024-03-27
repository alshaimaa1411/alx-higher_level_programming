#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    n_set = []
    for i in set_1:
        if i not in set_2:
            n_set.append(i)
    for a in set_2:
        if a not in set_1:
            n_set.append(a)
    return n_set
