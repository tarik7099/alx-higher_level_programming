#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list1 = []
    for new_matrix in matrix:
        new_list = []
        for new_matrix1 in new_matrix:
            value = new_matrix1 ** 2
            new_list.append(value)
        list1.append(new_list)
    return list1
