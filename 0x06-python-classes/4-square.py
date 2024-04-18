#!/usr/bin/python3
""" square class"""


class Square:
    """ class square"""
    def __int__(self, size=0):
        """ size attri """
        self.size = size

    @property
    def size(self):
        """ size attru"""
        return self.__size

    @size.setter
    def size(self, value):
        """value fun req """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return: size"""
        return self.__size * self.__size
