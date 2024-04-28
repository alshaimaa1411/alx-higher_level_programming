#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", "UTF8") as file:
        cont = file.read()
        print(cont)
