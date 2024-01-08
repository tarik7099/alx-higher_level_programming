#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds two numbers, a and b.

    Args:
    a (int or float): First number.
    b (int or float, optional): Second number. Defaults to 98.

    Returns:
    int: The addition of a and b as an integer.
    
    Raises:
    TypeError: If a or b is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
