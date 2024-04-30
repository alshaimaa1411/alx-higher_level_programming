#!/usr/bin/python3
import json
""" creat obj"""


def load_from_json_file(filename):
    """ creat obj"""
    with open(filename, "r", encoding="UTF8") as mfile:
        lfile = json.loads(mfile)
        return lfile
    