#!/usr/bin/python3
def uppercase(str):
    newstring = ""
    for i in str:
        if ord(str) >= 97 and ord(str) > 123:
            newstring += chr(ord(i) - 32)
        else:
            newstring += i
    print("{}".format(newstring))   
