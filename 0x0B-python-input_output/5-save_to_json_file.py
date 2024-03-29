#!/usr/bin/python3

"""Serialize an object and write"""


import json


def save_to_json_file(my_obj, filename):
    """Serialize an object to JSON and write to a file
    Args:
        my_obj(object):  Any serializable object
        file_name(str): The file to write
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
