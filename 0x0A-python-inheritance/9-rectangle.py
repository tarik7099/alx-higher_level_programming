#!/usr/bin/python3
"""BaseGeometry class Module"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate name and value
        Args:
            name(string)
            value(int)
        Raises:
            TypeError: if not isinstance(value, int)
            ValueError: if value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle  class"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

    def area(self):
        return self.__width * self.__height

    def __str__(self):

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
