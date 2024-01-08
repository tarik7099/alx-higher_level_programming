#!/usr/bin/python3

"""Defines a matrix division function."""


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
        raise TypeError("div must be a number")

    n_m = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of""
                                "integers/floats")
            if value == 0:
                raise ZeroDivisionError("division by zero")
            new_value = round(value / div, 2)
            new_row.append(new_value)
        n_m.append(new_row)
    return n_m
