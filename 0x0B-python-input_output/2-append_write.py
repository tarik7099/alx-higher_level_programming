#!/usr/bin/python3
""" read file """


def append_write(filename="", text=""):
    """
    Append a string to the end

    Parameters:
    - filename (str): The name
    - text (str): The string
    Returns:
    int: The number of characters
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_added = file.write(text)
        return characters_added
