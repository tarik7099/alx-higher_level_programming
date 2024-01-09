#!/usr/bin/python3

"""Write a function that returns True if the object is exactly"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class.

    Args:
    obj: The object to be checked.
    a_class: The class to check against.

    Returns:
    bool: True if the object is an instance False otherwise.
    """
    return type(obj) == a_class
