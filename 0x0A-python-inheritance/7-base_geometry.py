#!/usr/bin/python3
""" empty class"""


class BaseGeometry:
    """ e,pty class"""
    def area(self):
        """ exception aea"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value < 0:
            raise ValueError("<name> must be greater than 0")
