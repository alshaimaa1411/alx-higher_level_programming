#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = len(matrix)
    for i in range(0, a):
        b = len(matrix[i])
        for z in range(0, b):
            if z == (b - 1):
                print("{:d}".format(matrix[i][z]), end="")
            else:
                print("{:d}".format(matrix[i][z]), end=" ")
        print()
