#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    sum = 0
    for i in new_list:
        sum += i
    return sum
