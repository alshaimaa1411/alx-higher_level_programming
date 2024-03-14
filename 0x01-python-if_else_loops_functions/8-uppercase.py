#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(0, x):
        a = ord(str[i])
        if a in range(97, 123):
            b = a - 32
            print("{}".format(chr(b)), end="/n" if i == x else end="")
        else:
            print("{}".format(chr(a)), end="")
