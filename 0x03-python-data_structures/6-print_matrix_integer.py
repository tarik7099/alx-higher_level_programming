#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(3):
        if len(matrix) > i and len(matrix[i]) >= 3:
            print("{} {} {}".format(matrix[i][0], matrix[i][1], matrix[i][2]))