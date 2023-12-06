#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    list1= []
    
    for i in range(3):
        new_list= []
        for  j in range(3):
            #new_list= []
            value =matrix[i][j] ** 2
            new_list.append(value)
        list1.append(new_list)        
    return list1

    
#square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
