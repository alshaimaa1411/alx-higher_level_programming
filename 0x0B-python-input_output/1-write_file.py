#!/usr/bin/python3
""" write file"""


def write_file(filename="", text=""):
    """ write line"""
    with open(filename, "w", encoding="UTF8") as mfile:
        cont = mfile.write(text)
        words = text.split()
        for i in words:
            for x in i:
                chcount +=1
                print(chcount)

