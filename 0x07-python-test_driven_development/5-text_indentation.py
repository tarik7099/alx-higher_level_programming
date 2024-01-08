#!/usr/bin/python3


"""Write a function that prints a text with 2"""

def text_indentation(text):
    """
    Prints text with indentation after encountering certain punctuation marks.

    Args:
    text (str): The text to be processed.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end='')
        if char in (".", "?", ":"):
            print("\n")
        elif char == ' ':
            print(end='')
