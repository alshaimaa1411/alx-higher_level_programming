#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    if number < 0:
        n = (number % 10) * -1
    else:
        n = number % 10
    print(n, end="")
    return n
