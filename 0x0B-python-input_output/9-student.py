#!/usr/bin/python3

"""represent a student"""


class Student:
    """Defining student class """
    def __init__(self, first_name, last_name, age):
        """Student
        Args:
            first_name(str)
            last_name(str)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
