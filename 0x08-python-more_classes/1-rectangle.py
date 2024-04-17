#!/usr/bin/python3
""" rectangle class"""


class Rectangle:
    """ rectangle class
    Attributes:
    __width (int): rect width
    __hight (int): rect hight
    """
    def __init__(self, width=0, height=0):
        """ init rectanglr width - hight
        width (int): width
        hight (int): hight
        Return:
        None
        """
        self.width = width
        self.height = height

    def width(self):
        """
        width (int): width
        Return:
        width
        """
        return self.__width

    def width(self, value):
        """
        width req
        Return:
        value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    def height(self):
        """
        Return:
        height
        """
        return self.__height

    def height(self, value):
        """
        height (int): height
        Return:
        None
        """
        if type(value) is not int:
            raise TypeError("heigt must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
