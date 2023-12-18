#!/usr/bin/python3
def safe_print_integer(value):
    try:
        while value * 1 == value:
            print("{%d}".format(value), end='')
            return True
        else:
            return False
    except Exception as e:
        pass
