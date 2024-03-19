#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        x = len(matrix)
        for i in range(0, x):
            y = len(matrix[i])
            for z in range(0, y):
                print("{:d}".format(matrix[i][z]), end=" ")
            print()
            if i == x:
                print(end="")
