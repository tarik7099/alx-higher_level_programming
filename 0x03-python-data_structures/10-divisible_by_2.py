#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    myltiple_list = []
    for multiple in my_list:
        myltiple_list.append(multiple % 2 == 0)
    return myltiple_list
