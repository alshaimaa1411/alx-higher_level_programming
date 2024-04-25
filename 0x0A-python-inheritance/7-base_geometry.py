#!/usr/bin/python3
""" empty class"""


class BaseGeometry:
    """ e,pty class"""
    def area(self):
        """ exception aea"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ value exep"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".formar(name))
