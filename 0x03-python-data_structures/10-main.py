#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple = 2
    for i  in range(len(my_list)):
        if my_list[i] % 2 == 0:
            return my_list
        else:
            return False 
#divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1