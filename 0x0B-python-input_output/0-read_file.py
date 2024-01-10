#!/usr/bin/python3

""" read file """

def read_file(filename=""):
    with open(filename, encoding="UTF-8") as file:
        print(file.read())
