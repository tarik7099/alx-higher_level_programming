#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == "{:d}".format(value):
            return True
        else:
            return False
            #print("%d".format(value), end='')
        
    except Exception as e:
        pass
        

#safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

