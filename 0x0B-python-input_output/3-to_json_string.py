#!/usr/bin/python3
""" read file """

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation

    Parameters:
    - my_obj: The object
    Returns:
    str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
