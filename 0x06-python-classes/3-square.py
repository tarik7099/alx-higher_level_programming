#!/usr/bin/python3
""" class square """


class Square:
    """ class square with size """
    def __init__(self, size=0):
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
