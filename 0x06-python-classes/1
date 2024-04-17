#!/usr/bin/python3
''' square class '''


class Square:
    ''' square class
    size (int): size
    '''
    def __init__(self, size=0):
        ''' square fun
        __size : size
        '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            self.__size = size
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        ''' are fun
        __size square
        '''
        return self.__size ** 2
