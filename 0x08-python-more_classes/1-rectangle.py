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
        self.height = height
        self.width = width

    def height(self, value):
        """
        width req
        Return:
        value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                return self.__height = value

    def width(self, value):
        """
        width (int): width
        Return:
        None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                return self.__width = value
