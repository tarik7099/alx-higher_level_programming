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
    if issubclass(obj, a_class):
        return True
    else:
        return False
