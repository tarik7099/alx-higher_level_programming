#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9

def replace_in_list(my_list, idx, element):
    new_list = my_list[:]

    if idx < 0 or idx > len(my_list) - 1:
        return None
    new_list.insert(idx , element)
    del new_list[idx + 1]
    print(new_list)

if __name__ == "__main__":
    replace_in_list(my_list, idx, new_element)
