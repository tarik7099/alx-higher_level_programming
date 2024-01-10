#!/usr/bin/python3
""" read file """


import json


def from_json_string(my_str):
    """
    args:
        my_str(str)- Jsoon
    """
    if my_str:
        return json.loads(my_str)
