#!/usr/bin/python3
""" save json"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as mfile:
        j_obj = json.dumps(my_obj)
        mfile.write(j_obj)
        