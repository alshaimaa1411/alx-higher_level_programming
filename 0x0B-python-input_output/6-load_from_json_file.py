#!/usr/bin/python3
"""
function that creates an Obj”
"""

import json


def load_from_json_file(filename):
    """crate obj"""
    with open(filename, 'r', encoding='utf-8') as mfile:
        return json.load(mfile)
    
    