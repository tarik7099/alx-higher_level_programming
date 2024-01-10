#!/usr/bin/python3

"""represent a student"""


class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """Instantiates a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary

        Args:
            attrs (list): A list of strings

        Returns:
            dict: A dictionary containing
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key)
                    for key in attrs
                    if hasattr(self, key)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student

        Args:
            json (dict): A dictionary containing
        """
        for key, value in json.items():
            setattr(self, key, value)
