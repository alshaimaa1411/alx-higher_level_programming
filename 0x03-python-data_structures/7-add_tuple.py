#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    if a == 2 and b == 2:
        tuple_n = ((tuple_a[0]+tuple_b[0]), (tuple_a[1]+tuple_b[1]))
        return tuple_n
    elif b == 1:
        tuple_n = ((tuple_a[0]+tuple_b[0]), (tuple_a[1]+0))
        return tuple_n
    elif  a == 1:
        tuple_n = ((tuple_a[0]+tuple_b[0]), (tuple_b[1]+0))
        return tuple_n
    elif a == 0:
        return tuple_b
    else:
        return tuple_a
