#!/usr/bin/python3
class Square:
    ''' class square'''
    def __int__(self, size=0):
        ''' size attri '''
        self.size = size

    def area(self):
        '''area fun'''
        return self.__size ** 2

    def size(self):
        ''' size attru'''
        return self.__size

    def size(self, value):
        ''' value fun req '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
