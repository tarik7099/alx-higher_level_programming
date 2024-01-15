#!/usr/bin/python3

"""This module defines the Base class."""

import json


class Base:
    """Base class for handling objects."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class.

        Args:
            id (int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to be saved.
        """
        filename = f"{cls.__name__}.json"

        list_dictionaries = [obj.to_dictionary() for obj in (list_objs or [])]

        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): List of dictionaries to be converted.

        Returns:
            str: JSON-formatted string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): JSON-formatted string.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class and update it with a dictionary.

        Args:
            dictionary (dict): Dictionary to update the new instance with.

        Returns:
            object: New instance of the class.
        """
        if cls.__name__ == "Rectangle":
            du = cls(1, 1)
        elif cls.__name__ == "Square":
            du = cls(1)
        du.update(**dictionary)
        return du

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.json"

        with open(filename, 'r') as file:
            json_content = file.read()

            list_dicts = cls.from_json_string(json_content)

            instances = [cls.create(**d) for d in list_dicts]

            return instances
