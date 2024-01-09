#!/usr/bin/python3


"""Module containing inherits_from method"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance... """
    return isinstance(obj, a_class) and type(obj) != a_class
