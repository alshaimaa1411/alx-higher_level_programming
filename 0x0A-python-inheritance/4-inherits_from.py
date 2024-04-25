#!/usr/bin/python3
""" class """


def inherits_from(obj, a_class):
    """ return type"""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
