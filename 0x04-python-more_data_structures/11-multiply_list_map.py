def multiply_list_map(my_list=[], number=0):
    # Multiply each element in my_list by the number
    multiplied_list = list(map(lambda x: x * number, my_list))
    return multiplied_list
