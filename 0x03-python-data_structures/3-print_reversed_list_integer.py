#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[:]
    new_list.reverse()
    for i in range(len(new_list)):
        print("{:s}".format(new_list[i]))
