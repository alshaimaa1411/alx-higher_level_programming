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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ arae fun"""
        return self.__width * self.__height

    def __str__(self):
        """print w/h"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """ square class"""
    def __init__(self, size):
        """ init attri"""
        self.integer_validator("size", size)
        self.__size = size
        self.__init__(size, size)

    def area(self):
        """area fun"""
        return self.__size ** 2

    def __str__(self):
        """ print fun"""
        return "[[Square] {:d}/{:d}".formar(self.__size, self.__size)
