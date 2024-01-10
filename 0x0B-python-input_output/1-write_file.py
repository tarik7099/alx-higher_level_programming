#!/usr/bin/python3
""" read file """


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)
    Parameters:
    - filename (str): The name of the file
    - text (str): The string to be written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)
        return characters_written
