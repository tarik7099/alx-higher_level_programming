#!/usr/bin/python3

"""Write a function that returns the list of available attributes and methods"""

def lookup(obj):
    """
    Returns a list of available attributes
    Args:
    obj: An object to inspect.
    """
    return dir(obj)