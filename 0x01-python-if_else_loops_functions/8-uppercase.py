#!/usr/bin/python3
def uppercase(str):
    upstr = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            upstr += chr(ord(c) - 32)
    return upstr
