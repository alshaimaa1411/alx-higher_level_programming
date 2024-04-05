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
        if type(size) is int:
            if size < 0:
                raise ValueErorr('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeErorr('size must be an integer')
