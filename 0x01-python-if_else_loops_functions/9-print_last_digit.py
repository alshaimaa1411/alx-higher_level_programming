#!/usr/bin/python3
def print_last_digit(number):
    x = abs(number) % 10
    if x < 0:
        x = -x
    else:
        x = x
    return x
