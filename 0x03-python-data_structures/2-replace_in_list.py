#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]

idx = 3
new_element = 9
def replace_in_list(my_list, idx, element):
    new_list= []
    if idx < 0 or (idx > len(my_list) - 1):
        return None
    else:
            for i in range(len(my_list)):
        
                new_list.append(my_list[i])
            new_list.insert(idx , element)
            
            return new_list
