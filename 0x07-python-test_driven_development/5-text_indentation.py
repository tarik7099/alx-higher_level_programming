#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for new_txt in text:
        print(new_txt, end='') 
        if (new_txt == "." or new_txt == "?" or new_txt == ":"):
            
            print("\n")
            