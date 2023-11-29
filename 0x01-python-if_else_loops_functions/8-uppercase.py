i#!/usr/bin/python3
def uppercase(str):
    newstring = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            newstring += chr(ord(i) - 32)
        else:
            newstring += i
    print("{}".format(newstring))
