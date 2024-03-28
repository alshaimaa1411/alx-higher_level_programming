#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        n_li = []
        for key in a_dictionary.keys():
            value = a_dictionary[key]
            n_li.append(value)
        n_li = sorted(n_li)
        x = n_li[-1]
        for key in a_dictionary.keys():
            if x == a_dictionary[key]:
                print(key)
    else:
        return None
