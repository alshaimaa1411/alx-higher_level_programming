#!/usr/bin/python3
""" class reqtangle"""


class Rectangle:
    """ rectangle class"""
    def __init__(self, width=0, height=0):
        """ init width and height
        width (int): width
        heigtt (int): height
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ return: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ return: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ return area """
        return self.__height * self.__width

    def perimeter(self):
        """ return perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """ print triangle"""
        stri = ""
        if self.__height == 0 or self.__width == 0:
            print()
        else:
            stri += "\n".join("#" * self.__width for _ in range(self.__height))
        return stri
