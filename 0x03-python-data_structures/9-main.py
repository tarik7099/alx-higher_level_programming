#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]
    
    for numbers in my_list:
        if numbers > max_value:
            max_value = numbers
    return max_value
                      
    
                   
                
                
                


#ax_integer = __import__('9-max_integer').max_integer

my_list = [1,30, 90, 2, 13,200, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
