#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = my_list[:]

    if idx < 0 or idx > len(my_list) - 1:
        return None
    new_list.insert(idx , element)
    del new_list[idx + 1]
    return new_list
