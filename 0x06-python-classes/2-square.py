#!/usr/bin/python3
"""this is class square"""


class Square:
    """class square size=0"""
    def __init__(self, size=0):
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
