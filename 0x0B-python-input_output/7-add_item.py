#!/usr/bin/python3
import json
from sys import argv
""" add list"""


def save_to_json_file(my_obj, filename):
    """ write in file"""
    with open(filename, "w") as mfile:
        j_obj = json.dumps(my_obj)
        mfile.write(j_obj)
        
def load_from_json_file(filename):
    """crate obj"""
    with open(filename, 'r', encoding='utf-8') as mfile:
        return json.load(mfile)
    
def main():
    """ add list"""
    filename = "add_item.json"
    try:
        jlist = load_from_json_file(filename)
    except FileNotFoundError:
        jlist = []

    for arg in argv[1:]:
        jlist.append(arg)

    save_to_json_file(jlist, filename)
