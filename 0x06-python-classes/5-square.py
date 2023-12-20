#!/usr/bin/python3
""" class square """


class Square:
    """class square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size=0):
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        for j in range(0, self.size):
            for i in range(0, self.size):
                print("#", end="")
            print("")
