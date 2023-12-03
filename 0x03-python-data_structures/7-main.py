#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    
    
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        new_tuple_a = tuple_a[0] + tuple_b[0]
        new_tuple_b = tuple_a[1] + tuple_b[1]
        new_tuple_ab = (new_tuple_a, new_tuple_b)
        return new_tuple_ab
    elif len(tuple_b) == 1 :
        tuple_b = (tuple_b[0] , 0)
        new_tuple_a = tuple_a[0] + tuple_b[0]
        new_tuple_b = tuple_a[1] + tuple_b[1]
        new_tuple_ab = (new_tuple_a, new_tuple_b)
        return new_tuple_ab
    elif len(tuple_b) == 0:
        tuple_b = (0 , 0)
        new_tuple_a = tuple_a[0] + tuple_b[0]
        new_tuple_b = tuple_a[1] + tuple_b[1]
        new_tuple_ab = (new_tuple_a, new_tuple_b)
        return new_tuple_ab
    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]
        return tuple_a , tuple_b

#add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))