#!/usr/bin/python3
""" write file"""


def write_file(filename="", text=""):
    """ write line"""
    with open(filename, "w", encoding="UTF8") as mfile:
        cont = mfile.write(text)
        return len(text)
