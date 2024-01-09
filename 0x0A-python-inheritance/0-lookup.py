#!/usr/bin/python3


"""Write a function that returns the list"""


def lookup(obj):
    """
    Returns a list of available attributes
    Args:
    obj: An object to inspect.
    """
    return dir(obj)
