#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for new_list1 in my_list:
        new_list.append(new_list1)
    idx = new_list.index(search)
    new_list.insert(idx, replace)
    del new_list[idx + 1]
    return new_list
