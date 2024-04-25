#!/usr/bin/python3
""" class """


def is_inherited_instance(obj, base_class):
    """ return type"""
    return isinstance(obj, base_class) or issubclass(type(obj), base_class)
