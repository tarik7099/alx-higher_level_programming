#!/usr/bin/python3
"""BaseGeometry class Module"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):

        if isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
        