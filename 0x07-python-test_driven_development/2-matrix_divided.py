#!/usr/bin/python3

"""
This module provides a function to add two numbers and return their sum.
"""


def matrix_divided(matrix, div):
    """
    Divides each element in a matrix by a given number.

    Args:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The number to divide each element in the matrix by.

    Returns:
    list of lists: A new matrix with the divided elements.

    Raises:
    TypeError: If matrix is not a list of lists containing integers or floats.
    ValueError: If the divisor is not a number or if it's zero.
    """
    if not isinstance(div, (int, float)):
        TypeError("div must be a number")

    n_m = [[], []]
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for new_matrix in matrix[i]:
            if not isinstance(new_matrix, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if new_matrix == 0:
                raise ZeroDivisionError("division by zero")

            result = round(new_matrix / div, 2)
            n_m[i].append(result)
    return n_m
