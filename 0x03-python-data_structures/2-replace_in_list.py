#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
def replace_in_list(my_list, idx, element):
    new_list= []
    for i in range(len(my_list)):
        
        new_list.append(my_list[i])
    new_list.insert(idx , element)
    print(new_list)
if __name__ =="__main__":
    replace_in_list(my_list, idx, new_element)