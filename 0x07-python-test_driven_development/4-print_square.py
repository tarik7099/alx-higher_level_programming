#!/usr/bin/python3

"""Prints a square made"""


def print_square(size):
    """
    Prints a square made of '#' characters based on the given size.

    Args:
    size (int): The size of the square to be printed.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for squre  in range(size):
        print("#" * size)
