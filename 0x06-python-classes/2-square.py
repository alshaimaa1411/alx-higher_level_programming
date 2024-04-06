#!/usr/bin/python3
''' square class '''


class Square:
    '''
    int square
    size (int) : more than 0
    '''
    def __init__(self, size=0):
        ''' square fun
        __size : size of square
        '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            self.__size = size
        if size < 0:
            raise ValueError('size must be >= 0')
