#!/usr/bin/python3
def uniq_add(my_list=[]):
    value = 0
    new_list_no = []
    new_list = set(my_list)
    for item in new_list:
        new_list_no.append(item)
    for i in range(len(new_list_no)):

        value += new_list_no[i]

    return value
