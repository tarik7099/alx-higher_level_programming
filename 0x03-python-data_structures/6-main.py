#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix and len(matrix) > 1:
        for i in range(0 ,3):
            print("{} {} {}".format(matrix[i][0], matrix[i][1], matrix[i][2]))

                
            

#print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()