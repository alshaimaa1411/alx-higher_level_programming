#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a > 0:
        b = sentence[0]
        tup = (a, b)
    else:
        b = "None"
        tup = (a, b)
    return tup
