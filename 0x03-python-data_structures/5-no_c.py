#!/usr/bin/python3
def no_c(my_string):
    char_c = 'c'
    char_C = 'C'
    new_lis = []
    my_string_new = ""
    
    for i in range(0, len(my_string)):
        new_lis.append(my_string[i])
        # Remove all occurrences of 'c' from new_lis using list comprehension
    new_lis = [char for char in new_lis if char != char_c and (char != char_C)]
        
    my_string_new = "".join(new_lis)
    return my_string_new
