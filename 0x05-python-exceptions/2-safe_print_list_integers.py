#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        c = 0
        while i < x:
            print(my_list[c], end='')
            i += 1
    except (ValueError, TypeError):
        pass
    c += 0
    print()
    return i
