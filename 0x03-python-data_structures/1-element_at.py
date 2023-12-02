#!/usr/bin/python3

def element_at(my_list, idx):
    
    if idx < 0 or idx > len(my_list):
        return None
    else:
        for i in range(len(my_list)):
            if  my_list[idx] == my_list[i]:
                idxpass = my_list[i]
        return idxpass
