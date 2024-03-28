#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_key = sorted(a_dictionary.keys())
    b_dic = {key: a_dictionary[key] for key in s_key}
    for key, value in b_dic.items():
        print("{:s} : {:s}".format(str(key), str(value)))
