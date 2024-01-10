#!/usr/bin/python3
""" read file """


def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename

    Raises
        no

    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')
