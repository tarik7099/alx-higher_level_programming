#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    
    
    if matrix and len(matrix) >= 3:
        for i in range(3):
            if len(matrix[i]) >= 3:
                print("{:d} {:d} {:D}".format(matrix[i][0], matrix[i][1], matrix[i][2]))
    else:
        print()