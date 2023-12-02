#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[:]
    new_list.reverse()
    print("{:d}".format(new_list))
#print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)