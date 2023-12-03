#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i , column in enumerate(row):
            print(column, end=" ")
            if i != len(row) - 1:
                print("", end="")
            else:
                print(column, end="")
        print()