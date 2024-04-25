#!/usr/bin/python3
""" empty class"""


class BaseGeometry:
    """ e,pty class"""

    def area(self):
        """ exception aea"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ ractangle class"""

    def __init__(self, width, height):
        """ init attri"""
        super().integer_validator(name="width", value=width)
        super().integer_validator(name="height", value=height)
