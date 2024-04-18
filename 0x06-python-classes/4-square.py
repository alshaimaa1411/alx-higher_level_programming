#!/usr/bin/python3
""" square class"""


class Square:
    """ square class"""
    def __init__(self, size=0):
        """ attri size"""
        self.size = size

    def area(self):
        """ return area"""
        return self.__size ** 2

    @property
    def size(self):
        """ return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size req """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
