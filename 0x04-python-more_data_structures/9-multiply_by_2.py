#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dic = {key: a_dictionary[key] for key in a_dictionary.keys()}
    for key in b_dic.keys():
        value = int(b_dic[key])
        b_dic[key] = value * 2
    return b_dic
