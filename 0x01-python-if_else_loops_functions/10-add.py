#!/usr/bin/python3
def add(a, b):
    a = abs(a)
    b = abs(b)
    if a < 0 and b < 0:
        return -a - b
    elif a < 0 and b > 0:
        return -a + b
    elif a > 0 and b < 0:
        return a - b
    else:
        return a + b
