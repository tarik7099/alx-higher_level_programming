#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[len(tuple_b) - 1] , len(tuple_b) - 1)
    elif len(tuple_b) == 0:
        tuple_b = (len(tuple_b) , len(tuple_b))

    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result_tuple