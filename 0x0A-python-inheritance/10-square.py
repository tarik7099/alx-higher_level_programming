#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation of a square"""
    def __init__(self, size):
        """the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
