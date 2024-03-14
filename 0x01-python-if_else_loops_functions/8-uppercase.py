#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(0, x):
        a = ord(str[i])
        b = a - 32
        print("{}".format(chr(b)), end="")
