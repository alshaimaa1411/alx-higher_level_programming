#!/usr/bin/python3
""" sort list"""


class Mylist(list):
    """ sort list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ pint list"""
        print(sorted(self))
