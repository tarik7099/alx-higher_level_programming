#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    for j in range(len(my_list)):
        for i in range(len(my_list)):
            while my_list[j] < my_list[i]:
                max = my_list[i]
                return max
