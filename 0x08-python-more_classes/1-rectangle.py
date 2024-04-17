#!/usr/bin/python3
""" Retanglr class """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """
        width (int): recangle width
        height (int): rectangle height
        """
        self.height = height
        self.width = width

    def height(self):
        """return: height """
        return self.__height

    def height(self, value):
        """ height Error """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def width(self):
        """ return: width """
        return self.__width

    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
