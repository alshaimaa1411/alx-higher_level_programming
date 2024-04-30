#!/usr/bin/python3
""" student class"""


class Student:
    """ student class"""
    
    def __init__(self, first_name, last_name, age):
        """ atrri init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to json"""
        return self.__dict__
    
    def to_json(self, attrs=None):
        """ to json"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
