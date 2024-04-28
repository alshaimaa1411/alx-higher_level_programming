#!/usr/bin/python3
""" raed file"""


def read_file(filename=""):
    """ read file"""
    with open(filename, "r", encoding="UTF8") as file:
        cont = file.read()
        print(cont)
