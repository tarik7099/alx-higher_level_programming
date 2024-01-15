#!/usr/bin/python3

"""this is  class base"""

import json


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"

        list_dictionaries = [obj.to_dictionary() for obj in (list_objs or [])]

        json_string = cls.to_json_string(list_dictionaries)


        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_string)
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            du = cls(1, 1)
        if cls.__name__ == "Square":
            du = cls(1)
        du.update(**dictionary)
        return du
    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"

        with open(filename, 'r') as file:
            json_content = file.read()

            list_dicts = cls.from_json_string(json_content)

            instances = [cls.create(**d) for d in list_dicts]

            return instances