#!/usr/bin/python3
""" read file """


def to_json_string(my_obj):
    import json

    """
    Returns the JSON representation

    Parameters:
    - my_obj: The object
    Returns:
    str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
