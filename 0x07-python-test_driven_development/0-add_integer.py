#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds tow numbers,a and b

    args:
    a int
    b int
    Returns:
    int: The addition of a and b as an integer.    
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
