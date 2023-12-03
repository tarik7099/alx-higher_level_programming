#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    for j in range(len(my_list)):
        for i in range(len(my_list)):
            while my_list[j] < my_list[i]:
                max  = my_list[i]
                return max



#max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
