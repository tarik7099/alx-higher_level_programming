#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        cx = 0
        while i < x:
            print("{:d}".foramt(my_list[i]), end='')
            cx += 1
    except (ValueError, TypeError):
        pass
    i += 0
    print()
    return cx
