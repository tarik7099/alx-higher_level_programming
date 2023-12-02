#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return None
    my_list.insert(idx , element)
    del my_list[idx + 1]
    return my_list

if __name__=="__main__":
    hy =replace_in_list(my_list , idx , new_element)
    print(hy)