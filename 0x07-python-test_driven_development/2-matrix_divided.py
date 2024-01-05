#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not isinstance(div , (int, float)):
        TypeError ("div must be a number")
    n_m = [[], []]
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for new_matrix in matrix[i]:
            if not isinstance(new_matrix, (int ,float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if new_matrix == 0:
                raise ZeroDivisionError("division by zero")
            
            resulta = round(new_matrix / div, 2)
            n_m[i].append(resulta)
    return n_m            