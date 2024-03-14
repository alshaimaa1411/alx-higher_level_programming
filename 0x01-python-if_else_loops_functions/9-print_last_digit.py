#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = (number % 10) * -1
        return n
    else:
        n = number % 10
        return n
